import numpy
from dataclasses import dataclass

from SuPyMode.SuperSet              import SuperSet
from SuPyMode.Binary.SuperMode      import SuperMode as _SuperMode
from SuPyMode.Binary.CppSolver      import CppSolver as _CppSolver

from PyFinitDiff.Source import FiniteDifference2D




@dataclass
class SuPySolver(object):
    """ 
    This object corresponds to the solver.
    It solves the eigenvalues problems for a given geometry.

    """

    Geometry: None
    Tolerance : float = 1e-5
    MaxIter : int = 10000
    Accuracy: int = 2  
    Debug: bool = True
    IndexScrambling: float = None
    SolverNumber: int = 0

    def __post_init__(self):
        for core in self.Geometry.Objects:
            core.Index += numpy.random.rand(1)*self.IndexScrambling

        self.Geometry.CreateMesh()


    def InitBinding(self, Symmetries: dict, Wavelength: float, nComputedMode: int, nSortedMode: int): 
        self.FD = FiniteDifference2D(Nx         = self.Axes.x.N, 
                                     Ny         = self.Axes.y.N, 
                                     dx         = self.Axes.x.d, 
                                     dy         = self.Axes.y.d,
                                     Derivative = 2, 
                                     Accuracy   = self.Accuracy,
                                     Symmetries = Symmetries)


        self.FD.Compute()

        CppSolver = _CppSolver(Mesh          = self.Geometry._Mesh,
                               Gradient      = self.Geometry.Gradient().ravel(),
                               FinitMatrix   = self.FD.ToTriplet(),
                               nComputedMode = nComputedMode,
                               nSortedMode   = nSortedMode,
                               MaxIter       = self.MaxIter,
                               Tolerance     = self.Tolerance,
                               dx            = self.Axes.x.d,
                               dy            = self.Axes.y.d,
                               Wavelength    = Wavelength,
                               Debug         = self.Debug )

        CppSolver.SetSymmetries(**Symmetries)
        CppSolver.ComputeLaplacian()

        return CppSolver


    def CreateSuperSet(self, Wavelength: float, NStep: int, ITRi: float, ITRf: float):
        self.Wavelength = Wavelength
        self.NStep      = NStep
        self.ITRi       = ITRi
        self.ITRf       = ITRf
        self.ITRList    = numpy.linspace(ITRi, ITRf, NStep)
        self.Set        = SuperSet(ParentSolver=self)


    def AddModes(self, nComputedMode: int, nSortedMode: int, Symmetries: dict, Sorting: str = 'Index'):
        assert Sorting in ['Index', 'Field'], f"Incorrect sorting method: {Sorting}; Sorting can be ['Index', 'Field']"

        CppSolver  = self.InitBinding(Symmetries, self.Wavelength, nComputedMode, nSortedMode)

        CppSolver.LoopOverITR(ITR=self.ITRList, ExtrapolationOrder=3)

        CppSolver.SortModes(Sorting=Sorting)

        CppSolver.ComputeCouplingAdiabatic()


        for BindingNumber in range(CppSolver.nSortedMode):
            self.Set.AppendSuperMode(CppSolver=CppSolver, BindingNumber=BindingNumber, SolverNumber=self.SolverNumber)

        self.SolverNumber += 1


    def GetSet(self):
        return self.Set

    @property
    def Axes(self):
        return self.Geometry.Axes



# ---
