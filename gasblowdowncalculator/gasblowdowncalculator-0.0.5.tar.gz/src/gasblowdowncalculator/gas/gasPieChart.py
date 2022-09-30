# This file is part of GasBlowdownCalculator.

"""
.. module:: gas.gasPieChart
   :synopsis: Gas composition pie chart.

.. moduleauthor:: Michael Fischer
"""


# Python modules
from PyQt5 import QtGui, QtWidgets

from . import gasData


class GraphicsScenePie(QtWidgets.QGraphicsScene):
    """Gui: Gas composition pie chart.
    """

    def __init__(self):
        """Init gas composition pie chart.
        """

        QtWidgets.QGraphicsScene.__init__(self)

        # Rectangle size (ellipse within!)
        self.rectsize = 250

        # Angle factor
        self.anglefac = 16

        # Init
        self.initPieChart()

    def addPieToChart(self, angle, delAngle, color):
        """Add pie to pie chart.

        Parameters
        ----------
        angle : int
            Angle.
        delAngle : int
            Angle span.
        color : str
            Color string.
        """

        # Define circle geometry
        ellipse = QtWidgets.QGraphicsEllipseItem(0, 0, self.rectsize,
                                                 self.rectsize)
        ellipse.setPos(0, 0)

        # Draw colored pie (defined by start angle and angle span)
        ellipse.setStartAngle(min(angle, 361)*self.anglefac)
        ellipse.setSpanAngle(min(delAngle, 361)*self.anglefac)
        ellipse.setBrush(QtGui.QColor(color))
        self.addItem(ellipse)

    def initPieChart(self):
        """Init empty pie chart.
        """

        self.addPieToChart(0, 360, "white")

    def updatePieChart(self, gasComposition):
        """Update pie chart for a given gas composition.

        Parameters
        ----------
        gasComposition : dict
            Gas composition.
        """

        # Clear pie chart
        self.clear()

        # Empty pie chart for "empty" gas composition
        if (abs(sum(gasComposition.values())) <= gasData.EPSSUM_GAS):
            self.initPieChart()
            return

        # Add colored pies to pie chart based on gas composition fraction
        angle = 0   # start angle

        for ii in range(gasData.nDataTabGasComponents):

            delAngle = round(360*gasComposition[ii]/100.0)
            self.addPieToChart(angle, delAngle,
                               gasData.dataTabGasComponents[ii][1])
            angle = angle + delAngle

        # Rest: white pie (if gas composition incomplete)
        if (angle < 360):
            self.addPieToChart(angle, 360-angle, "white")
