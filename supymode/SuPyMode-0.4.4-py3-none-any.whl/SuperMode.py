#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy, logging
from dataclasses import dataclass
from typing import ClassVar
from SuPyMode.Binary.SuperMode import SuperMode as _SuperMode

try:
    from mayavi     import mlab
    from tvtk.tools import visual
except ImportError:
    logging.warning('Mayavi package could not be loaded! Not 3D rendering available.')


import SuPyMode.Plotting.Plots as Plots
import SuPyMode.Tools.Directories as Directories
from SuPyMode.Tools.BaseClass   import ReprBase
from SuPyMode.SuperSet import SuperSet
from SuPyMode.Binary.CppSolver import CppSolver as _CppSolver

@dataclass
class SuperMode(ReprBase):
    Description : ClassVar[str]  = 'Supermode class'
    ReprVar     : ClassVar[list] = ["ModeNumber", "BindingNumber", "ParentSet", "LeftSymmetry", "RightSymmetry", "TopSymmetry", "BottomSymmetry", "Size"]
    Methods     : ClassVar[list] = ["Fields", "Index", "Betas", "PlotIndex", "PlotBetas", "PlotPropagation"]

    ParentSet: SuperSet
    CppSolver: _CppSolver
    BindingNumber: int
    SolverNumber: int


    def __str__(self):
        return self.Name


    def __post_init__(self):
        self.Binded         = self.CppSolver.GetMode(self.BindingNumber)
        self.ID             = [self.SolverNumber, self.BindingNumber]
        self.Name           = f"Mode {self.SolverNumber}:{self.BindingNumber}"
        self._FullFields    = None
        self._Fields, self._Index, self._Betas, self._Adiabatic, self._Coupling = (None,)*5


    @property
    def ITR2Slice(self):
        return self.ParentSet.ITR2Slice

    @property
    def FullFields(self):
        if self._FullFields is None:
            self.ComputeFullFields()
        return self._FullFields


    @property
    def Adiabatic(self):
        if self._Adiabatic is None:
            self._Adiabatic = self.Binded.GetAdiabatic()

        return self._Adiabatic


    @property
    def Coupling(self):
        if self._Coupling is None:
            self._Coupling = self.Binded.GetCoupling()
        return self._Coupling


    @property
    def Fields(self):
        if self._Fields is None:
            self._Fields = self.Binded.GetFields()
        return self._Fields


    @property
    def Index(self):
        if self._Index is None:
            self._Index = self.Binded.GetIndex()
        return self._Index


    @property
    def Betas(self):
        if self._Betas is None:
            self._Betas = self.Binded.GetBetas()
        return self._Betas


    def AddTopFieldSymmetry(self, FullField):
        match self.TopSymmetry:
            case 0: return FullField

            case 1: return numpy.concatenate((FullField[:, :, ::-1], FullField), axis=2)

            case -1: return numpy.concatenate((-FullField[:, :, ::-1], FullField), axis=2)


    def AddBottomFieldSymmetry(self, FullField):
        match self.BottomSymmetry:
            case 0: return FullField

            case 1: return numpy.concatenate((FullField, FullField[:, :, ::-1]), axis=2)

            case -1: return numpy.concatenate((FullField, -FullField[:, :, ::-1]), axis=2)


    def AddLeftFieldSymmetry(self, FullField):
        match self.LeftSymmetry:
            case 0: return FullField

            case 1: return numpy.concatenate((FullField[...], FullField[:, ::-1, :]), axis=1) 

            case -1: return numpy.concatenate((FullField[...], -FullField[:, ::-1, :]), axis=1) 


    def AddRightFieldSymmetry(self, FullField):
        match self.RightSymmetry:
            case 0: return FullField

            case 1: return numpy.concatenate((FullField[:, ::-1, :], FullField[...]), axis=1) 

            case -1: return numpy.concatenate((-FullField[:, ::-1, :], FullField[...]), axis=1)


    def ComputeFullFields(self):
        self._FullFields = self.Fields

        self._FullFields = self.AddLeftFieldSymmetry(self._FullFields)

        self._FullFields = self.AddRightFieldSymmetry(self._FullFields)

        self._FullFields = self.AddTopFieldSymmetry(self._FullFields)

        self._FullFields = self.AddBottomFieldSymmetry(self._FullFields)


    def GetAdiabatic(self, Other=None):
        if Other is None:
            return self.Binded.GetAdiabatic()
        else:
            return self.Binded.GetAdiabaticSpecific(Other.Binded)


    def GetCoupling(self, Other=None):
        if Other is None:
            return self.Binded.GetCoupling()
        else:
            return self.Binded.GetCouplingSpecific(Other.Binded)


    def __render__index__(self, Figure, Ax):
        Figure.UnitSize = (10,4)
        Figure.Title    = ''
        Ax.yLabel       = r'Effective refraction index'
        Ax.xLabel       = 'ITR'

        artist = Plots.Line(X=self.ITRList, Y=self.Index, Label=self.Name)
        Ax.AddArtist( artist )


    def __render__beta__(self, Figure, Ax):
        Figure.UnitSize = (10,4)
        Ax.yLabel       = r'Propagation constante $\beta$'
        Ax.xLabel       = 'ITR'
        
        artist = Plots.Line(X=self.ITRList, Y=self.Betas, Label=self.Name)
        Ax.AddArtist( artist )
        

    def __render__adiabatic__(self, Figure, Ax, Other=None):
        Figure.UnitSize = (10,4)
        Ax.yLabel       = r'Adiabatic criterion'
        Ax.xLabel       = 'ITR'
        Ax.yLimits      = [1e-6, 1e-1]
        Ax.yScale       = 'log'

        if Other is None:
            for mode in self.ParentSet:
                self.__render__adiabatic__(Figure=Figure, Ax=Ax, Other=mode)

        else:
            artist = Plots.Line(X=self.ITRList, Y=self.GetAdiabatic(Other), Label=f'{self.Name} - {Other.Name}')
            Ax.AddArtist( artist )


    def __render__coupling__(self, Figure, Ax, Other=None):
        Figure.UnitSize = (10,4)
        Ax.yLabel       = r'Mode coupling'
        Ax.xLabel       = 'ITR'

        if Other is None:
            for mode in self.ParentSet:
                self.__render__coupling__(Figure=Figure, Ax=Ax, Other=mode)

        else:
            artist = Plots.Line(X=self.ITRList, Y=self.GetCoupling(Other), Label=f'{self.Name} - {Other.Name}')
            Ax.AddArtist( artist )


    def __render_field__(self, Figure, Ax, ITR: float=None, Slice: int=None):
        Figure.UnitSize = (3,3)
        Ax.yLabel   = r'Y-direction [$\mu m$]'
        Ax.xLabel   = r'X-Direction [$\mu m$]'
        Ax.Colorbar = Plots.ColorBar(Symmetric=True, Position='right')
        
        if ITR is not None:
            Ax.Title = f'{self.Name}  [ITR: {ITR:.2f}]'
            xAxis, yAxis = self.Axes.GetFullAxis(Symmetries=self.Symmetries)
            artist = Plots.Mesh(X=xAxis, Y=yAxis, Scalar=self.FullFields[self.ITR2Slice(ITR)], ColorMap=Plots.FieldMap)
            Ax.AddArtist( artist )

        if Slice is not None:
            Ax.Title = f'{self.Name}  [Slice: {Slice}]'
            xAxis, yAxis = self.Axes.GetFullAxis(Symmetries=self.Symmetries)
            artist = Plots.Mesh(X=xAxis, Y=yAxis, Scalar=self.FullFields[Slice], ColorMap=Plots.FieldMap)
            Ax.AddArtist( artist )


    def Plot(self, Type: str, **kwargs):
        Figure = Plots.Scene()
        Ax = Plots.Axis(Row=0, Col=0, Legend=True)
        Figure.AddAxes(Ax)

        match Type.lower():
            case 'index':
                self.__render__index__(Figure=Figure, Ax=Ax, **kwargs)
            case 'beta':
                self.__render__beta__(Figure=Figure, Ax=Ax, **kwargs)
            case 'coupling':
                self.__render__coupling__(Figure=Figure, Ax=Ax, **kwargs)
            case 'adiabatic':
                self.__render__adiabatic__(Figure=Figure, Ax=Ax, **kwargs)
            case 'field':
                self.__render_field__(Figure=Figure, Ax=Ax, **kwargs)

        return Figure




    @property
    def LeftSymmetry(self):
        return self.CppSolver.LeftSymmetry

    @property
    def RightSymmetry(self):
        return self.CppSolver.RightSymmetry

    @property
    def TopSymmetry(self):
        return self.CppSolver.TopSymmetry

    @property
    def BottomSymmetry(self):
        return self.CppSolver.BottomSymmetry

    @property
    def Size(self):
        return len(self.ParentSet.ITRList)

    @property
    def Geometry(self):
        return self.ParentSet.Geometry

    @property
    def ITRList(self):
        return self.ParentSet.ITRList

    @property
    def Axes(self):
        return self.ParentSet.Axes

    @property
    def yAxis(self):
        return self.Axes.Y

    @property
    def xAxis(self):
        return self.Axes.X

    @property
    def Symmetries(self):
        return {'Right': self.RightSymmetry, 'Left': self.LeftSymmetry, 'Top': self.TopSymmetry, 'Bottom': self.BottomSymmetry}


    def __getitem__(self, N):
        return self.Slice[N]


    def __setitem__(self, N, val):
        self.Slice[N] = val


    def GetArrangedFields(self):
        sign = numpy.sign( numpy.sum(self.FullFields[0]))
        FullFields = [sign*self.FullFields[0]]

        for field in self._FullFields:
            overlap = numpy.sum(field*FullFields[-1])
            if overlap > 0:
                FullFields.append(field/numpy.max(numpy.abs(field)))

            if overlap <= 0:
                FullFields.append(-field/numpy.max(numpy.abs(field)))

        return FullFields


    def PlotPropagation(self, SaveName=None):

        FullFields = self.GetArrangedFields()

        FileName = []

        factor = 5
        offset = 11

        fig = mlab.figure(size=(1000,700), bgcolor=(1,1,1), fgcolor=(0,0,0))

        surface = mlab.surf(FullFields[0]*factor + offset, colormap='coolwarm', warp_scale='4', representation='wireframe', line_width=6, opacity=0.9, transparent=True)

        mesh = self.Geometry.GetFullMesh(self.LeftSymmetry, self.RightSymmetry, self.TopSymmetry, self.BottomSymmetry)
        baseline = mlab.surf(mesh*0, color=(0,0,0), representation='wireframe', opacity=0.53)

        #mlab.contour_surf(mesh, color=(0,0,0), contours=[mesh.min(), 1.4, mesh.max()], line_width=6)

        mlab.axes( xlabel='x', ylabel='y', zlabel='z', color=(0,0,0), nb_labels=10, ranges=(0,40,0,40,0,20), y_axis_visibility=False )


        mlab.gcf().scene.parallel_projection = False
        mlab.view(elevation=70, distance=300)
        mlab.move(up=-6)

        #mlab.outline(baseline)


        import imageio

        @mlab.animate(delay=10)
        def anim_loc():
            for n, field in enumerate(FullFields):
                surface.mlab_source.scalars = field*factor + offset
                baseline.mlab_source.scalars = field*3


                if SaveName is not None:
                    FileName.append( f'{Directories.RootPath}/Animation/Animation_{n:03d}.png' )
                    mlab.savefig(filename=FileName[-1])

                yield

        anim_loc()
        mlab.show()


        if SaveName is not None:

            with imageio.get_writer(f'{Directories.RootPath}/Animation/{SaveName}.gif', mode='I', fps=50) as writer:
                for filename in FileName:
                    image = imageio.imread(filename)
                    writer.append_data(image)






# -
