# This file is part of GasBlowdownCalculator.

"""
.. module:: simulation
   :synopsis: Simulation.

.. moduleauthor:: Michael Fischer
"""


# Python modules
from .calculation import acc_LibBlowdownCalc


def simulate(gasprop, pipeData, valveData, orificeData, simData):

    # Blowdown
    blowdownR = acc_LibBlowdownCalc.Blowdown(gasprop,
                                             pipeData,
                                             valveData,
                                             orificeData,
                                             simData)

    # Run
    (resTime, resPressure, resLinepack, resFlow,
     resVelocity, resTlimCrit, resTlimSub, resTlimTot) = blowdownR.run()

    resAll = {
            "resTime": resTime,
            "resPressure": resPressure,
            "resLinepack": resLinepack,
            "resFlow": resFlow,
            "resVelocity": resVelocity,
            "resTlimCrit": resTlimCrit,
            "resTlimSub": resTlimSub,
            "resTlimTot": resTlimTot,
        }

    return (resAll)
