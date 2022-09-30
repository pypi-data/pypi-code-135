# This file is part of GasBlowdownCalculator.

"""
.. module:: calculation.acc_LibBlowdownCalc
   :synopsis: Blowdown calculation (accessing external DLL).

.. moduleauthor:: Michael Fischer
"""


# Python modules
import ctypes
import numpy
from scipy.integrate import odeint
import os
import sys

from . import acc_util

# Constants
DLL_NAME = 'LibBlowdownCalc.dll'

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

    prepare_blowdown = CalcDll.__blowdown_MOD_prepare_blowdown
    dpdt = CalcDll.__blowdown_MOD_dpdt
    calc_moutpipe = CalcDll.__blowdown_MOD_calc_moutpipe
    resultsblowdown = CalcDll.__blowdown_MOD_resultsblowdown

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

    prepare_blowdown.restype = ctypes.c_void_p
    prepare_blowdown.argtypes = [ctypes.c_double, ctypes.c_double,
                                 ctypes.c_double, ctypes.c_double,
                                 ctypes.c_double, ctypes.c_double,
                                 ctypes.c_int, ctypes.c_double,
                                 ctypes.c_double, ctypes.c_int]

    dpdt.restype = ctypes.c_double
    dpdt.argtypes = [ctypes.c_double, ctypes.c_double]

    calc_moutpipe.restype = ctypes.c_double
    calc_moutpipe.argtypes = [ctypes.c_double, ctypes.c_double]

    resultsblowdown.restype = ctypes.c_void_p
    resultsblowdown.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p,
                                ctypes.c_void_p, ctypes.c_void_p,
                                ctypes.c_void_p, ctypes.c_void_p,
                                ctypes.c_void_p, ctypes.c_void_p,
                                ctypes.c_void_p]

# else:   # Dlls missing
#     raise ImportError('Dlls missing')


class Blowdown(object):
    """ Blowdown calculation class.
    """

    def __init__(self, gas, pipeData, valveData, orificeData, simData):
        """Init blowdown system object for a given gas, pipe data, valve
        [and orifice data] as well as simulation data.

        Parameters
        ----------
        gas : calculation.acc_LibBwrCalc.Gas
            Gas object.
        pipeData : dict
            Pipe data: pipe diameter [m], pipe length [m], pipe
            start pressure [Pa], and temperature [K].
        valveData : dict
            Valve data: diameter of blowdown pipe [m] and Kv value.
        orificeData : dict
            Orifice data: orifice diameter [m].
        simData : dict
            Simulation data: Time interval [s] and time step [s].
        """

        # Input: gas
        psiVec = gas.psiVec

        # Input: pipe
        pipeDiameter = pipeData["pipeDiameter"]
        pipeLength = pipeData["pipeLength"]
        self._pipePressure = pipeData["pipePressure"]
        pipeTemperature = pipeData["pipeTemperature"]

        # Input: blowdown system (valve [+ orifice])
        blowdownDiameter = valveData["blowdownDiameter"]
        valveKv = valveData["valveKv"]

        if (len(orificeData) > 0):
            doOrifice = 1
            orificeDiameter = orificeData["orificeDiameter"]
        else:
            doOrifice = 0
            orificeDiameter = -1.0

        # Input: sim
        self._tmax = simData["tmax"]
        self._Nt = simData["Nt"]

        # Prepare gas
        nBasicProps = 1
        basicProps = numpy.zeros(nBasicProps)
        nNormProps = 9
        normProps = numpy.zeros(nNormProps)

        if (isInstalled):
            prepare_gas(psiVec.ctypes.data_as(ctypes.c_void_p),
                        basicProps.ctypes.data_as(ctypes.c_void_p),
                        normProps.ctypes.data_as(ctypes.c_void_p))

        # Prepare blowdown
        if (isInstalled):
            prepare_blowdown(pipeDiameter, pipeLength, self._pipePressure,
                             pipeTemperature, blowdownDiameter, valveKv,
                             doOrifice, orificeDiameter,
                             self._tmax, self._Nt)

    def solve(self):
        """Solve blowdown system differential equation.

        Returns
        -------
        t : numpy.array( float )
            Times [s].
        p : numpy.array( float )
            Pressures [s].
        """

        t = numpy.linspace(0.0, self._tmax, self._Nt)
        p = odeint(self.dpdt, self._pipePressure, t)

        return (t, p)

    def dpdt(self, p, t):
        """Calculate right-hand side for blowdown system differential equation.

        Returns
        -------
        dp/dt : float
            Derivative of pressure with respect to time [Pa/s].
        """

        if (isInstalled):
            return dpdt(p, t)
        else:
            return None

    def calc_mOutPipe(self, p, t):
        """Calculate pipe output mass flow based on blowdown system model
        (valve [, orifice]).

        Returns
        -------
        mout : float
            Pipe output mass flow [kg/s].
        """

        if (isInstalled):
            return calc_moutpipe(p, t)
        else:
            return None

    def run(self):
        """Run blowdown calculation.

        Returns
        -------
        t : numpy.array( float )
            Times [s].
        p : numpy.array( float )
            Pressures [bar].
        Linepack : numpy.array( float )
            Linepacks [m3].
        QN : numpy.array( float )
            Flows [Nm3/h].
        v : numpy.array( float )
            Flow velocities [m/s].
        Tlim_crit : float
            Blowdown time for overcritical valve phase [s].
        Tlim_sub : float
            Blowdown time for sub-critical valve phase [s].
        Tlim_tot : float
            Total blowdown time [s].
        """

        # Simulation
        (t, p) = self.solve()

        N = len(t)
        tnew = numpy.zeros(N)
        pnew = numpy.zeros(N)

        for ii in range(N):
            tnew[ii] = t[ii]
            pnew[ii] = p[ii]

        # Results
        pnewout = numpy.zeros(N)
        Linepack = numpy.zeros(N)
        QN = numpy.zeros(N)
        velocity = numpy.zeros(N)

        Tlim_crit = ctypes.c_double()
        Tlim_tot = ctypes.c_double()
        Tlim_sub = ctypes.c_double()

        if (isInstalled):
            resultsblowdown(N, tnew.ctypes.data_as(ctypes.c_void_p),
                            pnew.ctypes.data_as(ctypes.c_void_p),
                            pnewout.ctypes.data_as(ctypes.c_void_p),
                            Linepack.ctypes.data_as(ctypes.c_void_p),
                            QN.ctypes.data_as(ctypes.c_void_p),
                            velocity.ctypes.data_as(ctypes.c_void_p),
                            ctypes.byref(Tlim_crit),
                            ctypes.byref(Tlim_sub),
                            ctypes.byref(Tlim_tot))

        return (tnew, pnewout, Linepack, QN, velocity, Tlim_crit.value,
                Tlim_sub.value, Tlim_tot.value)
