# This file is part of GasBlowdownCalculator.

"""
.. module:: gas.gasComposition
   :synopsis: Gas composition.

.. moduleauthor:: Michael Fischer
"""


# Python modules
from PyQt5 import QtCore, QtGui, QtWidgets
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, parse
from xml.dom import minidom

# Own modules
from . import gasData
from . import gasPieChart


class GasComposition(QtCore.QObject):
    """ Gas composition.
        Gas composition part in the parent widget.
    """

    def __init__(self, parent, parentUi, inputModelCalc):
        """Initialize gas composition part of parent widget.

        Parameters
        ----------
        parent : QtGui.QMidget
            Parent widget object.
        parentUi : Ui
            Parent widget Qt ui.
        inputModelCalc : dataModelCalculation.InputModelCalc
            Input data model for calcultion object.
        """

        super(GasComposition, self).__init__()

        # Parent widget and parent widget Qt ui
        self._parent = parent
        self._parentUi = parentUi

        # Input data model for calculation
        self._inputModelCalc = inputModelCalc

        # Setup model-view (gas)
        self.setupTableModelGas()  # model
        self.setupTableViewGas()  # view

        # Init status message
        self.initLabelStatusGas()

        # Init model-view
        self.initTableModelGas()
        self.initGraphicsViewGas()

        # Signal-slot connects
        self.createConnects()

    def setupTableModelGas(self):
        """Setup table and selection model for gas composition.
        """

        # Setup table model ("generic model for storing custom data")
        self._modelGas = QtGui.QStandardItemModel(0, 2, self._parent)

        # Column header
        self._modelGas.setHeaderData(0, QtCore.Qt.Horizontal,
                                     "Component")
        self._modelGas.setHeaderData(1, QtCore.Qt.Horizontal,
                                     "Fraction [mol%]")

        # Setup table item selection model ("tracker of view's selected items")
        self._selectionModelGas = QtCore.QItemSelectionModel(self._modelGas)

    def setupTableViewGas(self):
        """Setup specific table view for gas.
        """

        # Set table models in view
        self._parentUi.tableViewGas.setModel(self._modelGas)
        self._parentUi.tableViewGas.setSelectionModel(self._selectionModelGas)

        # Header
        self._parentUi.tableViewGas.horizontalHeader().setResizeMode(
            QtWidgets.QHeaderView.Stretch)

    def initLabelStatusGas(self):
        """Init gas composition status message.
        """

        # Update status message
        self.updateLabelStatusGas(gasData.ID_STATUSGAS_FRACTIONSUM_OUTRANGE,
                                  {})

    def initTableModelGas(self):
        """Init table model for gas.
        """

        # Init gas components
        self.initGasComponents()

    def initGasComponents(self):
        """Init table model gas: fill table model with gas components and
        corresponding colors.
        """

        for ii in range(gasData.nDataTabGasComponents):

            self._modelGas.insertRows(ii, 1, QtCore.QModelIndex())
            self._modelGas.setData(
                self._modelGas.index(ii, 0, QtCore.QModelIndex()),
                QtGui.QColor(gasData.dataTabGasComponents[ii][1]),
                QtCore.Qt.DecorationRole)
            self._modelGas.setData(
                self._modelGas.index(ii, 0, QtCore.QModelIndex()),
                gasData.dataTabGasComponents[ii][0])
            self._modelGas.setData(
                self._modelGas.index(ii, 1, QtCore.QModelIndex()),
                float(0.0))

    def initGraphicsViewGas(self):
        """Init pie chart gas.
        """

        # Pie chart scene
        self.graphicsSceneGas = gasPieChart.GraphicsScenePie()

        # Set scene in view
        self._parentUi.graphicsViewGas.setScene(self.graphicsSceneGas)
        self._parentUi.graphicsViewGas.show()
        self._parentUi.graphicsViewGas.setEnabled(True)

    def updateLabelStatusGas(self, idStatus, gasComposition):
        """Update gas composition status message.

        Parameters
        ----------
        idStatus : int
            Status ID for gas composition.
        gasComposition : dict
            Gas composition.
        """

        if (idStatus == gasData.ID_STATUSGAS_OK):
            messg = "Gas composition is complete."
        elif (idStatus == gasData.ID_STATUSGAS_FRACTION_OUTRANGE):
            messg = "Gas composition contains invalid fractions."
        elif (idStatus == gasData.ID_STATUSGAS_FRACTIONSUM_OUTRANGE):
            messg = (
                "Gas composition incomplete: The sum of fractions is " +
                str("{0:.2f}".format(sum(gasComposition.values()))) + " mol%.")

        self._parentUi.labelStatusMessageGas.setText(str(messg))

    @QtCore.pyqtSlot()
    def updateGas(self):
        """Update gas composition - table, pie chart, status, input data model
        for calculation as well as simulation status.
        """

        # Get gas composition
        (gasComposition, idStatus) = self.getGasComponents()

        # Pie chart gas
        self.graphicsSceneGas.updatePieChart(gasComposition)

        # Label status gas
        self.updateLabelStatusGas(idStatus, gasComposition)

        # Block gas components name change
        self.resetGasComponentsName()

        # Input model calc
        if (idStatus == gasData.ID_STATUSGAS_OK):
            self._inputModelCalc.gasComposition = gasComposition
        else:
            self._inputModelCalc.gasComposition = None

        self._inputModelCalc.updateModelStatus()

    def resetGasComponentsName(self):
        """Reset gas components name if table cell is changed somehow.
        """

        for ii in range(gasData.nDataTabGasComponents):
            self._modelGas.setData(
                self._modelGas.index(ii, 0, QtCore.QModelIndex()),
                gasData.dataTabGasComponents[ii][0])

    @QtCore.pyqtSlot()
    def newGasComponents(self):
        """Reset gas composition.
        """

        for ii in range(gasData.nDataTabGasComponents):
            self._modelGas.setData(
                self._modelGas.index(ii, 1, QtCore.QModelIndex()),
                float(0.0))

    @QtCore.pyqtSlot()
    def readGasComponents(self):
        """Read gas composition from file.
        """

        fileName = QtWidgets.QFileDialog.getOpenFileName(self._parent,
                                                         filter='*.xml')
        if fileName:
            try:
                tree = parse(fileName[0])
                root = tree.getroot()
                for child in root:
                    ii = child.find('index').text
                    molfrac = child.find('molfrac').text
                    self._modelGas.setData(
                        self._modelGas.index(int(ii), 1, QtCore.QModelIndex()),
                        float(molfrac))
            except OSError as e:
                print("OS ERROR: ", e.errno)

    @QtCore.pyqtSlot()
    def saveGasComponents(self):
        """Save gas composition to file.
        """

        (gasComposition, idStatus) = self.getGasComponents()

        if (idStatus == gasData.ID_STATUSGAS_OK):

            # Generate xml structure
            top = Element('gasmixture')
            comment = Comment('Generated from GasPipeFlow')
            top.append(comment)
            for ii in range(gasData.nDataTabGasComponents):
                gascomp = gasData.dataTabGasComponents[ii][0]
                child = SubElement(top, 'gascomp')
                subchild_i = SubElement(child, 'index')
                subchild_i.text = str(ii)
                subchild_gascomp = SubElement(child, 'name')
                subchild_gascomp.text = gascomp
                subchild_molfrac = SubElement(child, 'molfrac')
                subchild_molfrac.text = str(gasComposition[ii])

            rough_string = tostring(top, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            xmldump = reparsed.toprettyxml(indent="\t")

            fileName = QtWidgets.QFileDialog.getSaveFileName(
                                self._parent, filter='*.xml')
            if fileName:
                try:
                    f = open(fileName[0], mode='w')
                    f.writelines(xmldump)
                    f.close()
                except OSError as e:
                    print("OS ERROR: ", e.errno)

    def getGasComponents(self):
        """Get gas composition from corresponding table model.
        """

        gasComposition = {}

        status = True
        idStatus = gasData.ID_STATUSGAS_OK

        for ii in range(gasData.nDataTabGasComponents):

            val = self._modelGas.data(
                       self._modelGas.index(ii, 1, QtCore.QModelIndex()),
                       float(0.0))

            gasComposition[ii] = val

            if (val < 0.0 or val > 100.0):
                status = False
                idStatus = gasData.ID_STATUSGAS_FRACTION_OUTRANGE

        if (status):
            if (abs(sum(gasComposition.values())-100.0) > gasData.EPSSUM_GAS):
                idStatus = gasData.ID_STATUSGAS_FRACTIONSUM_OUTRANGE

        return (gasComposition, idStatus)

    def createConnects(self):
        """Create signal-slot connections.
        """

        # Pie chart gas
        self._modelGas.itemChanged.connect(self.updateGas)

        # File operations gas
        self._parentUi.buttonNewGas.clicked.connect(self.newGasComponents)
        self._parentUi.buttonLoadGas.clicked.connect(self.readGasComponents)
        self._parentUi.buttonSaveGas.clicked.connect(self.saveGasComponents)
