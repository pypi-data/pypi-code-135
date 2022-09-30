#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy, os
from typing import ClassVar
from dataclasses import dataclass
from scipy.interpolate import interp1d


import SuPyMode.Tools.Directories as Directories
from SuPyMode.Tools.BaseClass import SetProperties, ReprBase
from SuPyMode.SuperPosition   import SuperPosition
import SuPyMode.Plotting.Plots as Plots

@dataclass
class SuperSet(SetProperties, ReprBase):
    Description: ClassVar[str]  = 'SuperSet class'
    ReprVar    : ClassVar[list] = ["ParentSolver", "Size", "Geometry"]
    Methods    : ClassVar[list] = ["GetSuperposition", "Matrix"]

    ParentSolver: None=None

    def __post_init__(self):
        self.SuperModes     = []
        self.Matrix         = None
        self.ITR2SliceIntero = interp1d( self.ITRList, numpy.arange(self.ITRList.size) )


    def ITR2Slice(self, ITR: float):
        return int(self.ITR2SliceIntero(ITR))


    def GetPropagationMatrix(self):
        self.Matrix = numpy.zeros([self.Size, self.Size, len(self.ITRList)])

        for mode in self.SuperModes:
            self.Matrix[mode.ModeNumber, mode.ModeNumber, :] = mode.Betas

        return self.Matrix


    @property
    def FullxAxis(self):
        if self._FullxAxis is None:
            self._FullxAxis, self._FullyAxis = self.GetFullAxis(self.Axes.X, self.Axes.Y)
        return self._FullxAxis


    @property
    def FullyAxis(self):
        if self._FullyAxis is None:
            self._FullxAxis, self._FullyAxis = self.GetFullAxis(self.Axes.X, self.Axes.Y)
        return self._FullyAxis


    def IterateSuperMode(self):
        for n, supermode in enumerate(self.SuperModes):
            yield supermode


    def ComputeM(self, CouplingFactor):
        shape = self.Beta.shape
        M     = numpy.zeros( [shape[0], shape[1], shape[1]] )
        for iter in range(shape[0]):
            beta = self.Beta[iter]
            M[iter] = CouplingFactor[iter] * self.Coupling[iter] + beta * numpy.identity(shape[1])

        return M


    def ComputeCouplingFactor(self, Length):
        dx =  Length/(self.Geometry.ITRList.size)

        dITR = numpy.gradient(numpy.log(self.Geometry.ITRList), 1)

        return dITR/dx


    def GetSuperposition(self, Amplitudes):
        return SuperPosition(SuperSet=self, InitialAmplitudes=Amplitudes)


    def Propagate(self, Amplitude=[1,1, 0, 0, 0], Length=1000):
        Amplitude = numpy.asarray(Amplitude)

        Distance = numpy.linspace(0, Length, self.ITRList.size)

        #Factor = self.ComputeCouplingFactor(Length)

        #M = self.ComputeM(CouplingFactor=Factor)

        Minterp = interp1d(Distance, self.Matrix, axis=-1)

        def foo(t, y):
            return 1j * Minterp(t).dot(y)

        sol = solve_ivp(foo,
                        y0       = Amplitude.astype(complex),
                        t_span   = [0, Length],
                        method   = 'RK45')

        return sol.y


    def Propagate_(self, Amplitude, Length, **kwargs):
        Amplitude = numpy.asarray(Amplitude)

        Distance = numpy.linspace(0, Length, self.Geometry.ITRList.size)

        Factor = self.ComputeCouplingFactor(Length)

        M = self.ComputeM(CouplingFactor=Factor)

        Minterp = interp1d(Distance, M, axis=0)

        def foo(t, y):
            return 1j * Minterp(t).dot(y)

        sol = solve_ivp(foo,
                        y0       = Amplitude.astype(complex),
                        t_span   = [0, Length],
                        method   = 'RK45',
                        **kwargs)

        return sol

    @property
    def Size(self):
        return len(self.SuperModes)

    @property
    def Geometry(self):
        return self.ParentSolver.Geometry

    @property
    def ITRList(self):
        return self.ParentSolver.ITRList

    @property
    def Axes(self):
        return self.ParentSolver.Geometry.Axes


    def AppendSuperMode(self, CppSolver, BindingNumber, SolverNumber):
        from SuPyMode.SuperMode import SuperMode
        superMode = SuperMode(ParentSet=self, CppSolver=CppSolver, BindingNumber=BindingNumber, SolverNumber=SolverNumber )

        self.SuperModes.append( superMode )


    def __getitem__(self, N):
        return self.SuperModes[N]


    def __setitem__(self, N, val):
        self.SuperModes[N] = val



    def PlotIndex(self):
        Figure = Plots.Scene()

        Ax = Plots.Axis(Row=0, Col=0, Legend=True)

        for supermode in self.SuperModes:
            supermode.__render__index__(Figure=Figure, Ax=Ax)

        Figure.AddAxes(Ax)

        return Figure


    def PlotBeta(self):
        Figure = Plots.Scene()

        Ax = Plots.Axis(Row=0, Col=0, Legend=True)

        for supermode in self.SuperModes:
            supermode.__render__beta__(Figure=Figure, Ax=Ax)

        Figure.AddAxes(Ax)

        return Figure



    def PlotCoupling(self, ModeOfInterest=None):
        Figure = Plots.Scene()
        Ax = Plots.Axis(Row=0, Col=0, Legend=True)

        for Mode0, Mode1 in self.GetCombinations():
            if ModeOfInterest and Mode0.ID not in ModeOfInterest and Mode1.ID not in ModeOfInterest:
                continue

            else:
                Mode0.__render__coupling__(Figure=Figure, Ax=Ax, Other=Mode1)

        Figure.AddAxes(Ax)

        return Figure


    def PlotAdiabatic(self, ModeOfInterest=None):
        Figure = Plots.Scene()
        Ax = Plots.Axis(Row=0, Col=0, Legend=True)

        for Mode0, Mode1 in self.GetCombinations():

            if ModeOfInterest and Mode0.ID not in ModeOfInterest and Mode1.ID not in ModeOfInterest:
                continue
            else:
                Mode0.__render__adiabatic__(Figure=Figure, Ax=Ax, Other=Mode1)

        Figure.AddAxes(Ax)

        return Figure



    def GetCombinations(self):
        Combination = []
        for Mode0 in self.SuperModes:
            for Mode1 in self.SuperModes:
                if Mode0.SolverNumber != Mode1.SolverNumber: 
                    continue

                if Mode0.BindingNumber == Mode1.BindingNumber: 
                    continue

                if (Mode1, Mode0) in Combination: 
                    continue

                Combination.append((Mode0, Mode1))

        return Combination



    def PlotField(self, ITR: list=[], Slice: list=[]):
        Figure = Plots.Scene(UnitSize = (3,3))

        if len(ITR) != 0:
            for m, Mode in enumerate(self.SuperModes):
                for n, itr in enumerate(ITR):
                    Ax = Plots.Axis(Row=n, Col=m, Equal=True)
                    Figure.AddAxes(Ax)

                    self[m].__render_field__(Figure=Figure, Ax=Ax, ITR=itr)

            return Figure

        if len(Slice) != 0:
            for m, Mode in enumerate(self.SuperModes):
                for n, slc in enumerate(Slice):
                    Ax = Plots.Axis(Row=n, Col=m, Equal=True)
                    Figure.AddAxes(Ax)

                    self[m].__render_field__(Figure=Figure, Ax=Ax, Slice=slc)

            return Figure


    def Plot(self, Type: str, **kwargs):
        match Type.lower():
            case 'index':
                return self.PlotIndex(**kwargs)
            case 'beta':
                return self.PlotBeta(**kwargs)
            case 'coupling':
                return self.PlotCoupling(**kwargs)
            case 'adiabatic':
                return self.PlotAdiabatic(**kwargs)
            case 'field':
                return self.PlotField(**kwargs)


    def GetReport(self, ITR: list=[1], dpi: int=300, Filename :str='ReportTest', ModeOfInterest: list=None):
        Figures = []
        Figures.append( self.Geometry.Plot().Render() )

        Figures.append( self.PlotField(ITR=ITR).Render() )

        Figures.append( self.PlotIndex().Render() )

        Figures.append( self.PlotBeta().Render() )

        Figures.append( self.PlotCoupling(ModeOfInterest=None).Render() )

        Figures.append( self.PlotAdiabatic(ModeOfInterest=None).Render() )

        directory = os.path.join(Directories.ReportPath, Filename) + '.pdf'

        Plots.Multipage(directory, figs=Figures, dpi=dpi)














# - 
