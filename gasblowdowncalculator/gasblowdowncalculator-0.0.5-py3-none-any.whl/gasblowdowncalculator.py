# This file is part of GasBlowdownCalculator.

"""
.. module:: gasblowdowncalculator
   :synopsis: Graphical user interace module.

.. moduleauthor:: Michael Fischer
"""


# Python modules
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph

from .calculation import acc_LibBwrCalc
from .gas import gasComposition
from .results import results
from . import ui

from . import dataModelCalculation
from .simulation import simulate


def run():
    """GUI main loop.
    """

    # Plot background change
    pyqtgraph.setConfigOption('background', 'w')
    pyqtgraph.setConfigOption('foreground', 'k')

    # App
    app = QtWidgets.QApplication(sys.argv)

    mainwindow = GBCMainWindow()
    mainwindow.showMaximized()

    sys.exit(app.exec_())


class GBCMainWindow(QtWidgets.QMainWindow):
    """GUI: Main window.
    """

    def __init__(self, *args):

        QtWidgets.QMainWindow.__init__(self, *args)

        self.ui = ui.ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # Activate stylesheet use for centralwidget
        self.ui.centralwidget.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.setWindowTitle("GasBlowdownCalculator")

        # Data models for calculation
        self.inputModelCalc = dataModelCalculation.InputModelCalc()
        self.outputModelCalc = dataModelCalculation.OutputModelCalc()

        # Gas composition
        self.gasComposition = gasComposition.GasComposition(
            self, self.ui, self.inputModelCalc)

        # Results
        self.resultsView = results.ResultsView(
            self, self.ui, self.outputModelCalc)

        # Signal-slot connects
        self.createConnects()

        # Signal-slot connects Scenario
        self.createConnectsScenario()

        # Scenario validators
        self.setValidatorLineeditsScenario()

        # Init Scenario lineedits
        self.initLineeditsScenario()

        # Init pages
        self.initPages()

        # Further inits
        self.ui.radioButtonWithoutOrifice.setChecked(True)
        self.showPageWithoutOrifice()

        # Sim
        self.initSimulation()

    def createConnects(self):
        """Setup signal-slot connections.
        """

        # Input model calc
        self.inputModelCalc.modelStatusInputSignal.connect(
            self.updateStatusSim)

        # Navigation
        self.ui.buttonGasComposition.clicked.connect(
            self.showPageGasComposition)
        self.ui.buttonScenario.clicked.connect(self.showPageScenario)
        self.ui.buttonResults.clicked.connect(self.showPageResults)

        self.ui.radioButtonWithOrifice.clicked.connect(
            self.showPageWithOrifice)
        self.ui.radioButtonWithoutOrifice.clicked.connect(
            self.showPageWithoutOrifice)

        # Simulation
        self.ui.buttonStartSim.clicked.connect(self.startSimulation)

    def initPages(self):
        """Gui: start pages"""

        self.showPageGasComposition()

    @QtCore.pyqtSlot()
    def showPageGasComposition(self):

        ind = self.ui.stackedWidgetMain.indexOf(self.ui.pageGasComposition)
        self.ui.stackedWidgetMain.setCurrentIndex(ind)

        self.uncheckNavigationButtons()
        self.ui.buttonGasComposition.setChecked(True)

    @QtCore.pyqtSlot()
    def showPageScenario(self):

        ind = self.ui.stackedWidgetMain.indexOf(self.ui.pageScenario)
        self.ui.stackedWidgetMain.setCurrentIndex(ind)

        self.uncheckNavigationButtons()
        self.ui.buttonScenario.setChecked(True)

    @QtCore.pyqtSlot()
    def showPageResults(self):

        ind = self.ui.stackedWidgetMain.indexOf(self.ui.pageResults)
        self.ui.stackedWidgetMain.setCurrentIndex(ind)

        self.uncheckNavigationButtons()
        self.ui.buttonResults.setChecked(True)

    def uncheckNavigationButtons(self):
        """Gui: Uncheck all navigation buttons"""

        self.ui.buttonGasComposition.setChecked(False)
        self.ui.buttonScenario.setChecked(False)
        self.ui.buttonResults.setChecked(False)

    @QtCore.pyqtSlot()
    def showPageWithOrifice(self):

        ind = self.ui.stackedWidgetOrifice.indexOf(self.ui.pageWithOrifice)
        self.ui.stackedWidgetOrifice.setCurrentIndex(ind)

    @QtCore.pyqtSlot()
    def showPageWithoutOrifice(self):

        ind = self.ui.stackedWidgetOrifice.indexOf(self.ui.pageWithoutOrifice)
        self.ui.stackedWidgetOrifice.setCurrentIndex(ind)

    def initSimulation(self):

        # Simulation status
        self.ui.labelStatusMessageSim.setText(str("Await parameter input."))

        # Deactivate start button, deactivate stop button
        self.ui.buttonStartSim.setEnabled(False)

    def updateStatusSim(self, statusModel):

        if (statusModel):
            messg = "Ready for simulation."
            self.ui.buttonStartSim.setEnabled(True)

        else:
            messg = "Await parameter input."
            self.ui.buttonStartSim.setEnabled(False)

        self.ui.labelStatusMessageSim.setText(str(messg))

    def startSimulation(self):

        # Parameters: gas
        gascomp = {}
        for ii in self.inputModelCalc.gasComposition.keys():
            name = acc_LibBwrCalc.gasComponentsInds[ii]
            gascomp[name] = self.inputModelCalc.gasComposition[ii]

        gasprop = acc_LibBwrCalc.Gas(gascomp)

        # Parameters: pipe
        pipeData = {"pipeDiameter": self.inputModelCalc.pipeDiameter/1000.0,
                    "pipeLength": self.inputModelCalc.pipeLength,
                    "pipePressure": self.inputModelCalc.pipePressure*1.0e5,
                    "pipeTemperature":
                        self.inputModelCalc.pipeTemperature + 273.15,
                    }

        # Parameters: valve
        valveData = {"blowdownDiameter":
                     self.inputModelCalc.blowdownDiameter/1000.0,
                     "valveKv": self.inputModelCalc.valveKv,
                     }

        # Parameters: orifice
        isPresentOrifice = self.inputModelCalc.isPresentOrifice
        if (isPresentOrifice):
            orificeData = {"orificeDiameter":
                           self.inputModelCalc.orificeDiameter/1000.0,
                           }
        else:
            orificeData = {}

        # Parameters: sim
        simData = {"tmax": self.inputModelCalc.timeInterval,
                   "Nt": int(self.inputModelCalc.timeInterval /
                             self.inputModelCalc.timestep),
                   }

        # Setup simulation
        self.ui.labelStatusMessageSim.setText(str("Simulation running."))

        resAll = simulate(gasprop, pipeData, valveData, orificeData, simData)
        self.finishSimulation(resAll)

    def finishSimulation(self, resAll):

        self.outputModelCalc.resTime = resAll["resTime"]
        self.outputModelCalc.resPressure = resAll["resPressure"]
        self.outputModelCalc.resLinepack = resAll["resLinepack"]
        self.outputModelCalc.resFlow = resAll["resFlow"]
        self.outputModelCalc.resVelocity = resAll["resVelocity"]
        self.outputModelCalc.resTlimCrit = resAll["resTlimCrit"]
        self.outputModelCalc.resTlimSub = resAll["resTlimSub"]
        self.outputModelCalc.resTlimTot = resAll["resTlimTot"]

        # Update status label
        self.ui.labelStatusMessageSim.setText(str("Simulation finished."))

        # Update results
        self.resultsView.update()

    def updatePipeDiameter(self):
        """Update pipe diameter.
        """

        val = float(
            self.ui.lineEditPipeDiameter.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.pipeDiameter = val
        else:
            self.inputModelCalc.pipeDiameter = None

        self.inputModelCalc.updateModelStatus()

    def updatePipeDiameter2(self):

        valStr = self.ui.lineEditPipeDiameter.text()
        if (len(valStr) == 0):
            self.inputModelCalc.pipeDiameter = None

        self.inputModelCalc.updateModelStatus()

    def updatePipeLength(self):
        """Update pipe length.
        """

        val = float(
            self.ui.lineEditPipeLength.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.pipeLength = val
        else:
            self.inputModelCalc.pipeLength = None

        self.inputModelCalc.updateModelStatus()

    def updatePipeLength2(self):

        valStr = self.ui.lineEditPipeLength.text()
        if (len(valStr) == 0):
            self.inputModelCalc.pipeLength = None

        self.inputModelCalc.updateModelStatus()

    def updatePipePressure(self):
        """Update pipe start pressure.
        """

        val = float(
            self.ui.lineEditStartPressure.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.pipePressure = val
        else:
            self.inputModelCalc.pipePressure = None

        self.inputModelCalc.updateModelStatus()

    def updatePipePressure2(self):

        valStr = self.ui.lineEditStartPressure.text()
        if (len(valStr) == 0):
            self.inputModelCalc.pipePressure = None

        self.inputModelCalc.updateModelStatus()

    def updatePipeTemperature(self):
        """Update pipe temperature.
        """

        val = float(
            self.ui.lineEditTemperature.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.pipeTemperature = val
        else:
            self.inputModelCalc.pipeTemperature = None

        self.inputModelCalc.updateModelStatus()

    def updatePipeTemperature2(self):

        valStr = self.ui.lineEditTemperature.text()
        if (len(valStr) == 0):
            self.inputModelCalc.pipeTemperature = None

        self.inputModelCalc.updateModelStatus()

    def updateBlowdownDiameter(self):
        """Update blowdown pipe diameter.
        """

        val = float(
            self.ui.lineEditBlowPipeDiameter.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.blowdownDiameter = val
        else:
            self.inputModelCalc.blowdownDiameter = None

        self.inputModelCalc.updateModelStatus()

    def updateBlowdownDiameter2(self):

        valStr = self.ui.lineEditBlowPipeDiameter.text()
        if (len(valStr) == 0):
            self.inputModelCalc.blowdownDiameter = None

        self.inputModelCalc.updateModelStatus()

    def updateValveKv(self):
        """Update valve Kv value.
        """

        val = float(
            self.ui.lineEditValveKv.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.valveKv = val
        else:
            self.inputModelCalc.valveKv = None

        self.inputModelCalc.updateModelStatus()

    def updateValveKv2(self):

        valStr = self.ui.lineEditValveKv.text()
        if (len(valStr) == 0):
            self.inputModelCalc.valveKv = None

        self.inputModelCalc.updateModelStatus()

    def updateIsPresentOrifice(self):
        """Update presence status of orifice.
        """

        isWithOrifice = self.ui.radioButtonWithOrifice.isChecked()
        isWithoutOrifice = self.ui.radioButtonWithoutOrifice.isChecked()

        if (isWithOrifice and not (isWithoutOrifice)):
            self.inputModelCalc.isPresentOrifice = True
        elif (not (isWithOrifice) and isWithoutOrifice):
            self.inputModelCalc.isPresentOrifice = False

        self.inputModelCalc.updateModelStatus()

    def updateOrificeDiameter(self):
        """Update orifice diameter.
        """

        val = float(
            self.ui.lineEditOrificeDiameter.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.orificeDiameter = val
        else:
            self.inputModelCalc.orificeDiameter = None

        self.inputModelCalc.updateModelStatus()

    def updateOrificeDiameter2(self):

        valStr = self.ui.lineEditOrificeDiameter.text()
        if (len(valStr) == 0):
            self.inputModelCalc.orificeDiameter = None

        self.inputModelCalc.updateModelStatus()

    def updateTimeInterval(self):
        """Update simulation time interval.
        """

        val = float(
            self.ui.lineEditSimTimeInterval.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.timeInterval = val
        else:
            self.inputModelCalc.timeInterval = None

        self.inputModelCalc.updateModelStatus()

    def updateTimeInterval2(self):

        valStr = self.ui.lineEditSimTimeInterval.text()
        if (len(valStr) == 0):
            self.inputModelCalc.timeInterval = None

        self.inputModelCalc.updateModelStatus()

    def updateTimestep(self):
        """Update simulation time step.
        """

        val = float(
            self.ui.lineEditSimTimestep.text().replace(',', '.'))
        if (val > 0.0):
            self.inputModelCalc.timestep = val
        else:
            self.inputModelCalc.timestep = None

        self.inputModelCalc.updateModelStatus()

    def updateTimestep2(self):

        valStr = self.ui.lineEditSimTimestep.text()
        if (len(valStr) == 0):
            self.inputModelCalc.timestep = None

        self.inputModelCalc.updateModelStatus()

    def createConnectsScenario(self):
        """Create signal-slot connections.
        """

        self.ui.lineEditPipeDiameter.editingFinished.connect(
            self.updatePipeDiameter)
        self.ui.lineEditPipeLength.editingFinished.connect(
            self.updatePipeLength)
        self.ui.lineEditStartPressure.editingFinished.connect(
            self.updatePipePressure)
        self.ui.lineEditTemperature.editingFinished.connect(
            self.updatePipeTemperature)
        self.ui.lineEditBlowPipeDiameter.editingFinished.connect(
            self.updateBlowdownDiameter)
        self.ui.lineEditValveKv.editingFinished.connect(
            self.updateValveKv)
        self.ui.lineEditOrificeDiameter.editingFinished.connect(
            self.updateOrificeDiameter)
        self.ui.lineEditSimTimeInterval.editingFinished.connect(
            self.updateTimeInterval)
        self.ui.lineEditSimTimestep.editingFinished.connect(
            self.updateTimestep)

        self.ui.lineEditPipeDiameter.textEdited.connect(
            self.updatePipeDiameter2)
        self.ui.lineEditPipeLength.textEdited.connect(
            self.updatePipeLength2)
        self.ui.lineEditStartPressure.textEdited.connect(
            self.updatePipePressure2)
        self.ui.lineEditTemperature.textEdited.connect(
            self.updatePipeTemperature2)
        self.ui.lineEditBlowPipeDiameter.textEdited.connect(
            self.updateBlowdownDiameter2)
        self.ui.lineEditValveKv.textEdited.connect(
            self.updateValveKv2)
        self.ui.lineEditOrificeDiameter.textEdited.connect(
            self.updateOrificeDiameter2)
        self.ui.lineEditSimTimeInterval.textEdited.connect(
            self.updateTimeInterval2)
        self.ui.lineEditSimTimestep.textEdited.connect(
            self.updateTimestep2)

        self.ui.radioButtonWithOrifice.clicked.connect(
            self.updateIsPresentOrifice)
        self.ui.radioButtonWithoutOrifice.clicked.connect(
            self.updateIsPresentOrifice)

    def initLineeditsScenario(self):
        """Init lineedits.
        """

        self.ui.lineEditPipeDiameter.setText(str(0.0))
        self.ui.lineEditPipeLength.setText(str(0.0))
        self.ui.lineEditStartPressure.setText(str(0.0))
        self.ui.lineEditTemperature.setText(str(0.0))
        self.ui.lineEditBlowPipeDiameter.setText(str(0.0))
        self.ui.lineEditValveKv.setText(str(0.0))
        self.ui.lineEditOrificeDiameter.setText(str(0.0))
        self.ui.lineEditSimTimeInterval.setText(str(0.0))
        self.ui.lineEditSimTimestep.setText(str(0.0))

    def setValidatorLineeditsScenario(self):
        """Create validators for lineedits.
        """

        # Validator
        self.validator = QtGui.QDoubleValidator()
        self.validator.setBottom(0.0)

        # Set validator
        self.ui.lineEditPipeDiameter.setValidator(self.validator)
        self.ui.lineEditPipeLength.setValidator(self.validator)
        self.ui.lineEditStartPressure.setValidator(self.validator)
        self.ui.lineEditTemperature.setValidator(self.validator)
        self.ui.lineEditBlowPipeDiameter.setValidator(self.validator)
        self.ui.lineEditValveKv.setValidator(self.validator)
        self.ui.lineEditOrificeDiameter.setValidator(self.validator)
        self.ui.lineEditSimTimeInterval.setValidator(self.validator)
        self.ui.lineEditSimTimestep.setValidator(self.validator)
