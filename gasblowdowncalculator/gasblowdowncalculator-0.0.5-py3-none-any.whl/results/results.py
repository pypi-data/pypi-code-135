# This file is part of GasBlowdownCalculator.

"""
.. module:: results.results
   :synopsis: Results.

.. moduleauthor:: Michael Fischer
"""


# Python modules
from PyQt5 import QtCore
import pyqtgraph


class ResultsView(object):
    """ Results view.
    """

    def __init__(self, parent, parentUi, outputModelCalc):
        """Initialize results view.

        Parameters
        ----------
        parent : QtGui.QMidget
            Parent widget object.
        parentUi : Ui
            Parent widget Qt ui.
        outputModelCalc : dataModelCalculation.OutputModelCalc
            Ouput data model for calcultion object.
        """

        # Parent: main window
        self._parent = parent
        self._parentUi = parentUi

        # Input model calc
        self._outputModelCalc = outputModelCalc

        # Init
        self.initBlowdownTimeLabels()
        self.initDiagrams()

    def initBlowdownTimeLabels(self):
        """Init blowdown time labels.
        """

        # Blowdown time labels
        self._parentUi.labelResCritical.setText(str(-1) + " s")
        self._parentUi.labelResSubCritical.setText(str(-1) + " s")
        self._parentUi.labelResTotal.setText(str(-1) + " s")

    def initDiagrams(self):
        """Init results diagrams for pressure, linepack, flow,
        and flow velocity.
        """

        # Disable mouse interaction with axes
        self._parentUi.graphicsViewResultsPressure.setMouseEnabled(x=False,
                                                                   y=False)
        self._parentUi.graphicsViewResultsLinepack.setMouseEnabled(x=False,
                                                                   y=False)
        self._parentUi.graphicsViewResultsFlow.setMouseEnabled(x=False,
                                                               y=False)
        self._parentUi.graphicsViewResultsVelocity.setMouseEnabled(x=False,
                                                                   y=False)

        # Add plots
        self._parentUi.graphicsViewResultsPressure.plot()
        self._parentUi.graphicsViewResultsLinepack.plot()
        self._parentUi.graphicsViewResultsFlow.plot()
        self._parentUi.graphicsViewResultsVelocity.plot()

        # Enable automatic rescaling
        self._parentUi.graphicsViewResultsPressure.enableAutoRange()
        self._parentUi.graphicsViewResultsLinepack.enableAutoRange()
        self._parentUi.graphicsViewResultsFlow.enableAutoRange()
        self._parentUi.graphicsViewResultsVelocity.enableAutoRange()

        # Hide auto-scale buttons
        self._parentUi.graphicsViewResultsPressure.hideButtons()
        self._parentUi.graphicsViewResultsLinepack.hideButtons()
        self._parentUi.graphicsViewResultsFlow.hideButtons()
        self._parentUi.graphicsViewResultsVelocity.hideButtons()

        # Empty diagrams
        self.emptyDiagrams()

    def emptyDiagrams(self):
        """Provide empty results diagrams for pressure, linepack, flow,
        and flow velocity.
        """

        # x axis labels
        self._parentUi.graphicsViewResultsPressure.setLabel('bottom', 'Time',
                                                            units='s')
        self._parentUi.graphicsViewResultsLinepack.setLabel('bottom', 'Time',
                                                            units='s')
        self._parentUi.graphicsViewResultsFlow.setLabel('bottom', 'Time',
                                                        units='s')
        self._parentUi.graphicsViewResultsVelocity.setLabel('bottom', 'Time',
                                                            units='s')

        # y axis labels
        self._parentUi.graphicsViewResultsPressure.setLabel('left', 'Pressure',
                                                            units='bar')
        self._parentUi.graphicsViewResultsLinepack.setLabel('left', 'Linepack',
                                                            units='m³')
        self._parentUi.graphicsViewResultsFlow.setLabel('left', 'Flow',
                                                        units='m³/h')
        self._parentUi.graphicsViewResultsVelocity.setLabel('left',
                                                            'Flow velocity',
                                                            units='m/s')

        # Dummy xrange
        self._parentUi.graphicsViewResultsPressure.setXRange(0.0, 1.0)
        self._parentUi.graphicsViewResultsLinepack.setXRange(0.0, 1.0)
        self._parentUi.graphicsViewResultsFlow.setXRange(0.0, 1.0)
        self._parentUi.graphicsViewResultsVelocity.setXRange(0.0, 1.0)

        # Dummy yrange
        self._parentUi.graphicsViewResultsPressure.setYRange(0.0, 1.0)
        self._parentUi.graphicsViewResultsLinepack.setYRange(0.0, 1.0)
        self._parentUi.graphicsViewResultsFlow.setYRange(0.0, 1.0)
        self._parentUi.graphicsViewResultsVelocity.setYRange(0.0, 1.0)

        # Enable automatic scaling
        self._parentUi.graphicsViewResultsPressure.enableAutoRange()
        self._parentUi.graphicsViewResultsLinepack.enableAutoRange()
        self._parentUi.graphicsViewResultsFlow.enableAutoRange()
        self._parentUi.graphicsViewResultsVelocity.enableAutoRange()

    @QtCore.pyqtSlot()
    def update(self):
        """Update results: blowdown time labels diagrams for pressure,
        linepack, flow, and flow velocity.
        """

        # Blowdown time labels
        self._parentUi.labelResCritical.setText(
            str(int(self._outputModelCalc.resTlimCrit)) + " s")
        self._parentUi.labelResSubCritical.setText(
            str(int(self._outputModelCalc.resTlimSub)) + " s")
        self._parentUi.labelResTotal.setText(
            str(int(self._outputModelCalc.resTlimTot)) + " s")

        # Clear plots
        self._parentUi.graphicsViewResultsPressure.plotItem.clear()
        self._parentUi.graphicsViewResultsLinepack.plotItem.clear()
        self._parentUi.graphicsViewResultsFlow.plotItem.clear()
        self._parentUi.graphicsViewResultsVelocity.plotItem.clear()

        # Fill plots
        self._parentUi.graphicsViewResultsPressure.plot(
            self._outputModelCalc.resTime,
            self._outputModelCalc.resPressure,
            pen=pyqtgraph.mkPen('r', width=3))

        self._parentUi.graphicsViewResultsLinepack.plot(
            self._outputModelCalc.resTime,
            self._outputModelCalc.resLinepack,
            pen=pyqtgraph.mkPen('r', width=3))

        self._parentUi.graphicsViewResultsFlow.plot(
            self._outputModelCalc.resTime,
            self._outputModelCalc.resFlow,
            pen=pyqtgraph.mkPen('r', width=3))

        self._parentUi.graphicsViewResultsVelocity.plot(
            self._outputModelCalc.resTime,
            self._outputModelCalc.resVelocity,
            pen=pyqtgraph.mkPen('r', width=3))
