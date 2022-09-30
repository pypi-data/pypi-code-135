# This file is part of GasBlowdownCalculator.

"""
.. module:: calculation.acc_LibBwrCalc
   :synopsis: Gas property calculation (accessing external DLL).

.. moduleauthor:: Michael Fischer
"""


# Python modules
import ctypes
import numpy
import os
import sys

from . import acc_util

# Constants
DLL_NAME = 'LibBwrCalc.dll'

# Access to installation of LibBlowdownCalc via environment variable
(dirInstalled, isInstalled) = acc_util.isLibInstalled()

# Alternative access to package folder
if (isInstalled is False):

    if getattr(sys, 'frozen', False):
        dirname = os.path.dirname(sys.executable)
    elif __file__:
        dirname = os.path.dirname(__file__)

    (dirInstalled, isInstalled) = acc_util.isLibInFolder(dirname)

# Dll import
if (isInstalled):   # Dlls accessible

    print("Dlls accessible from: ", dirInstalled)

    # Dll path
    dll_path = os.path.join(dirInstalled, DLL_NAME)

    # Dll
    CalcDll = ctypes.cdll.LoadLibrary(dll_path)

    # Lib functions
    prepare_gas = CalcDll.__bwrlib_MOD_prepare_gas

    calc_realgasfactor_z = CalcDll.__bwrlib_MOD_calc_realgasfactor_z
    calc_compressibility_k = CalcDll.__bwrlib_MOD_calc_compressibility_k
    calc_compressibility_kt = CalcDll.__bwrlib_MOD_calc_compressibility_kt
    calc_compressibility_kp = CalcDll.__bwrlib_MOD_calc_compressibility_kp
    calc_rho = CalcDll.__bwrlib_MOD_calc_rho
    calc_eos_rho = CalcDll.__bwrlib_MOD_calc_eos_rho
    calc_cv = CalcDll.__bwrlib_MOD_calc_cv
    calc_cp = CalcDll.__bwrlib_MOD_calc_cp
    calc_kappa = CalcDll.__bwrlib_MOD_calc_kappa
    calc_csound = CalcDll.__bwrlib_MOD_calc_csound

    # Data type interfaces
    prepare_gas.restype = ctypes.c_void_p
    prepare_gas.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

    calc_realgasfactor_z.restype = ctypes.c_double
    calc_realgasfactor_z.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_compressibility_k.restype = ctypes.c_double
    calc_compressibility_k.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_compressibility_kt.restype = ctypes.c_double
    calc_compressibility_kt.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_compressibility_kp.restype = ctypes.c_double
    calc_compressibility_kp.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_rho.restype = ctypes.c_double
    calc_rho.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_eos_rho.restype = ctypes.c_double
    calc_eos_rho.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]

    calc_cv.restype = ctypes.c_double
    calc_cv.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_cp.restype = ctypes.c_double
    calc_cp.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_kappa.restype = ctypes.c_double
    calc_kappa.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_csound.restype = ctypes.c_double
    calc_csound.argtypes = [ctypes.c_double, ctypes.c_double]

# else:   # Dlls missing
#     raise ImportError('Dlls missing')


# Physical constants
R_UNI = 0.08206     # universal gas constant [atm*m^3/kmol*K]
TNORM = 273.15      # normal temperature [K]
PNORM = 101325.0    # normal pressure [Pa]

# Gas component indexing/order:
gasComponentsInds = {
    0: "methane",
    1: "ethane",
    2: "propane",
    3: "isobutane",
    4: "n-butane",
    5: "isopentane",
    6: "n-pentane",
    7: "n-hexane",
    8: "n-heptane",
    9: "n-octane",
    10: "n-nonane",
    11: "n-decane",
    12: "hydrogen sulfide",
    13: "nitrogen",
    14: "oxygen",
    15: "hydrogen",
    16: "carbon dioxide",
    17: "carbon monoxide",
    18: "helium",
    19: "argon",
}

nGasComponentsInds = len(gasComponentsInds)


class Gas(object):
    """ Gas class.
        This class contains several methods for the calculation of
        gas properties for a given gas composition.
    """

    def __init__(self, gascomposition):
        """Init gas object for a given gas composition.

        Parameters
        ----------
        gascomposition : dict
            The gas composition: { name1 : frac1, ... }.
        """

        # Gas composition
        self._gascomposition = gascomposition
        self._ngascomp = len(gascomposition)

        # Index list
        self.trafo_gasCompositionToVectors()

        # Prepare gas
        nBasicProps = 1
        basicProps = numpy.zeros(nBasicProps)
        nNormProps = 9
        normProps = numpy.zeros(nNormProps)

        if (isInstalled):
            prepare_gas(self._psiVec.ctypes.data_as(ctypes.c_void_p),
                        basicProps.ctypes.data_as(ctypes.c_void_p),
                        normProps.ctypes.data_as(ctypes.c_void_p))

        self._R = basicProps[0]

        self._ZN = normProps[0]
        self._KN = normProps[1]
        self._KTN = normProps[2]
        self._KpN = normProps[3]
        self._rhoN = normProps[4]
        self._cvN = normProps[5]
        self._cpN = normProps[6]
        self._kappaN = normProps[7]
        self._cSoundN = normProps[8]

    def trafo_gasCompositionToVectors(self):
        """Transform gas composition dict data to vector data.
        """

        # Init vector data
        self._psiVec = numpy.zeros(nGasComponentsInds)

        # Fill
        for ind in range(nGasComponentsInds):

            name = gasComponentsInds[ind]
            if (name in self._gascomposition.keys()):
                self._psiVec[ind] = self._gascomposition[name]
            else:
                self._psiVec[ind] = 0.0

        # Normalize molar fractions
        self._psiVec = self._psiVec*1.0/numpy.sum(self._psiVec)

    def calc_realGasFactor_Z(self, p, T):
        """Calculate real gas factor Z.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        Z : float
            Real gas factor.
        """

        if (isInstalled):
            return calc_realgasfactor_z(p, T)
        else:
            return 0.0

    def calc_compressibility_K(self, p, T):
        """Calculate compressibility K.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        K : float
            Compressibility.
        """

        if (isInstalled):
            return calc_compressibility_k(p, T)
        else:
            return 0.0

    def calc_compressibility_KT(self, p, T):
        """Calculate compressibility KT.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        KT : float
            Compressibility.
        """

        if (isInstalled):
            return calc_compressibility_kt(p, T)
        else:
            return 0.0

    def calc_compressibility_Kp(self, p, T):
        """Calculate compressibility Kp.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        Kp : float
            Compressibility.
        """

        if (isInstalled):
            return calc_compressibility_kp(p, T)
        else:
            return 0.0

    def calc_rho(self, p, T):
        """Calculate density.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        rho : float
            Density [kg/m3].
        """

        if (isInstalled):
            return calc_rho(p, T)
        else:
            return 0.0

    def calc_eos_rho(self, Z, p, T):
        """Calculate density.

        Parameters
        ----------
        Z : float
            Real gas factor.
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        rho : float
            Density [kg/m3].
        """

        if (isInstalled):
            return calc_eos_rho(Z, p, T)
        else:
            return 0.0

    def calc_cv(self, p, T):
        """Calculate specific heat capacity cv.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        cv : float
            Specific heat capacity cv [J/kg*K].
        """

        if (isInstalled):
            return calc_cv(p, T)
        else:
            return 0.0

    def calc_cp(self, p, T):
        """Calculate specific heat capacity cp.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        cp : float
            Specific heat capacity cp [J/kg*K].
        """

        if (isInstalled):
            return calc_cp(p, T)
        else:
            return 0.0

    def calc_kappa(self, p, T):
        """Calculate isentropic exponent.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        kappa : float
            Isentropic exponent.
        """

        if (isInstalled):
            return calc_kappa(p, T)
        else:
            return 0.0

    def calc_cSound(self, p, T):
        """Calculate speed of sound.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        c : float
            Speed of sound [m/s].
        """

        if (isInstalled):
            return calc_csound(p, T)
        else:
            return 0.0

    @property
    def psiVec(self):
        """Fraction vector.
        """
        return self._psiVec

    @property
    def gascomposition(self):
        """Gas composition.
        """

        return self._gascomposition

    @property
    def ngascomp(self):
        """Number of gas components in gas composition.
        """

        return self._ngascomp

    @property
    def basicProp_R(self):
        """Basic property: specific gas constant R [J/kg*K].
        """

        return self._R

    @property
    def normProp_ZN(self):
        """Norm property: real gas factor Z in norm state.
        """

        return self._ZN

    @property
    def normProp_KN(self):
        """Norm property: compressibility K in norm state.
        """

        return self._KN

    @property
    def normProp_KTN(self):
        """Norm property: compressibility KT in norm state.
        """

        return self._KTN

    @property
    def normProp_KpN(self):
        """Norm property: compressibility Kp in norm state.
        """

        return self._KpN

    @property
    def normProp_rhoN(self):
        """Norm property: density rho [kg/m3] in norm state.
        """

        return self._rhoN

    @property
    def normProp_cvN(self):
        """Norm property: specific heat capacity cv [J/kg*K] in norm state.
        """

        return self._cvN

    @property
    def normProp_cpN(self):
        """Norm property: specific heat capacity cp [J/kg*K] in norm state.
        """

        return self._cpN

    @property
    def normProp_kappaN(self):
        """Norm property: isentropic exponent in norm state.
        """

        return self._kappaN

    @property
    def normProp_cSoundN(self):
        """Norm property: speed of sound [m/s] in norm state.
        """

        return self._cSoundN
