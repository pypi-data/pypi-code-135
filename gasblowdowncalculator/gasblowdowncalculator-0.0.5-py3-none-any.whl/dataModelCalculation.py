# This file is part of GasBlowdownCalculator.

"""
.. module:: dataModelCalculation
   :synopsis: Data model for calculation.

.. moduleauthor:: Michael Fischer
"""


# Python modules
from PyQt5 import QtCore


class InputModelCalc(QtCore.QObject):
    """Input data model for calculation.
    """

    # Signal: model status (completeness)
    modelStatusInputSignal = QtCore.pyqtSignal(bool)

    def __init__(self):
        """Initialize input data model for calculation.
        """

        super(InputModelCalc, self).__init__()

        # Gas composition
        self._gasComposition = None

        # Pipe
        self._pipeDiameter = None
        self._pipeLength = None
        self._pipePressure = None
        self._pipeTemperature = None

        # Blowdown system (valve [+ orifice])
        self._blowdownDiameter = None
        self._valveKv = None

        # Orifice
        self._isPresentOrifice = False
        self._orificeDiameter = None

        # sim
        self._timeInterval = None
        self._timestep = None

    def updateModelStatus(self):
        """Update model status (completeness).
        """

        modelStatus = ((self._gasComposition is not None) and
                       (self._pipeDiameter is not None) and
                       (self._pipeLength is not None) and
                       (self._pipePressure is not None) and
                       (self._pipeTemperature is not None) and
                       (self._blowdownDiameter is not None) and
                       (self._valveKv is not None) and
                       (not (self._isPresentOrifice) or
                            (self._isPresentOrifice and
                                (self._orificeDiameter is not None))) and
                       (self._timeInterval is not None) and
                       (self._timestep is not None))

        self.modelStatusInputSignal.emit(modelStatus)

    @property
    def gasComposition(self):
        """Gas composition.
        """

        return self._gasComposition

    @gasComposition.setter
    def gasComposition(self, value):
        """Set gas composition.
        """

        self._gasComposition = value

    @property
    def pipeDiameter(self):
        """Pipe diameter [mm].
        """

        return self._pipeDiameter

    @pipeDiameter.setter
    def pipeDiameter(self, value):
        """Set pipe diameter [mm].
        """

        self._pipeDiameter = value

    @property
    def pipeLength(self):
        """Pipe length [m].
        """

        return self._pipeLength

    @pipeLength.setter
    def pipeLength(self, value):
        """Set pipe length [m].
        """

        self._pipeLength = value

    @property
    def pipePressure(self):
        """Pipe start pressure [bar].
        """

        return self._pipePressure

    @pipePressure.setter
    def pipePressure(self, value):
        """Set pipe start pressure [bar].
        """

        self._pipePressure = value

    @property
    def pipeTemperature(self):
        """Pipe temperature [°C].
        """

        return self._pipeTemperature

    @pipeTemperature.setter
    def pipeTemperature(self, value):
        """Set pipe temperature [°C].
        """

        self._pipeTemperature = value

    @property
    def blowdownDiameter(self):
        """Blowdown pipe diameter [mm].
        """

        return self._blowdownDiameter

    @blowdownDiameter.setter
    def blowdownDiameter(self, value):
        """Set blowdown pipe diameter [mm].
        """

        self._blowdownDiameter = value

    @property
    def valveKv(self):
        """Valve Kv value.
        """

        return self._valveKv

    @valveKv.setter
    def valveKv(self, value):
        """Set valve Kv value.
        """

        self._valveKv = value

    @property
    def isPresentOrifice(self):
        """Presence status of orifice.
        """

        return self._isPresentOrifice

    @isPresentOrifice.setter
    def isPresentOrifice(self, value):
        """Set presence status of orifice.
        """

        self._isPresentOrifice = value

    @property
    def orificeDiameter(self):
        """Orifice diameter [mm].
        """

        return self._orificeDiameter

    @orificeDiameter.setter
    def orificeDiameter(self, value):
        """Set orifice diameter [mm].
        """

        self._orificeDiameter = value

    @property
    def timeInterval(self):
        """Simulation time interval [s].
        """

        return self._timeInterval

    @timeInterval.setter
    def timeInterval(self, value):
        """Set simulation time interval [s].
        """

        self._timeInterval = value

    @property
    def timestep(self):
        """Simulation time step [s].
        """

        return self._timestep

    @timestep.setter
    def timestep(self, value):
        """Set simulation time step [s].
        """

        self._timestep = value


class OutputModelCalc(QtCore.QObject):
    """Output data model for calculation.
    """

    # Signal: model status (completeness)
    modelStatusOutputSignal = QtCore.pyqtSignal(bool)

    def __init__(self):
        """Initialize output data model for calculation.
        """

        super(OutputModelCalc, self).__init__()

        self._resTime = None
        self._resPressure = None
        self._resLinepack = None
        self._resFlow = None
        self._resVelocity = None

        self._resTlimCrit = None
        self._resTlimSub = None
        self._resTlimTot = None

    def updateModelStatus(self):
        """Update model status (completeness).
        """

        modelStatus = (self._resTime is not None)

        self.modelStatusOutputSignal.emit(modelStatus)

    @property
    def resTime(self):
        """Time array [s].
        """

        return self._resTime

    @resTime.setter
    def resTime(self, value):
        """Set time array [s].
        """

        self._resTime = value

    @property
    def resPressure(self):
        """Pressure array [bar].
        """

        return self._resPressure

    @resPressure.setter
    def resPressure(self, value):
        """Set pressure array [bar].
        """

        self._resPressure = value

    @property
    def resLinepack(self):
        """Linepack array [m³].
        """

        return self._resLinepack

    @resLinepack.setter
    def resLinepack(self, value):
        """Set linepack array [m³].
        """

        self._resLinepack = value

    @property
    def resFlow(self):
        """Flow array [Nm³/h].
        """

        return self._resFlow

    @resFlow.setter
    def resFlow(self, value):
        """Set flow array [Nm³/h].
        """

        self._resFlow = value

    @property
    def resVelocity(self):
        """Flow velocity array [m/s].
        """

        return self._resVelocity

    @resVelocity.setter
    def resVelocity(self, value):
        """Set flow velocity array [m/s].
        """

        self._resVelocity = value

    @property
    def resTlimCrit(self):
        """Overcritical blowdown time [s].
        """

        return self._resTlimCrit

    @resTlimCrit.setter
    def resTlimCrit(self, value):
        """Set overcritical blowdown time [s].
        """

        self._resTlimCrit = value

    @property
    def resTlimSub(self):
        """Sub-critical blowdown time [s].
        """

        return self._resTlimSub

    @resTlimSub.setter
    def resTlimSub(self, value):
        """Set sub-critical blowdown time [s].
        """

        self._resTlimSub = value

    @property
    def resTlimTot(self):
        """Total blowdown time [s].
        """

        return self._resTlimTot

    @resTlimTot.setter
    def resTlimTot(self, value):
        """Set total blowdown time [s].
        """

        self._resTlimTot = value
