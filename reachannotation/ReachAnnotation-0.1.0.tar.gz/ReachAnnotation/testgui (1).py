from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Multimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Ui_MainWindow(object):
    # def __init__(self, args):
          #self.blah = MainWindow
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 140, 131, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 430, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 71, 16))
        self.label_2.setObjectName("label_2")

        # path_widget
        # video_widget update
        # text widgets
        # integrate path_widget function into GUI



        # load in video
        # video, behavior_times, classification_ids = load_data(path_from_widget)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(290, 40, 361, 221))
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 20, 61, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(320, 270, 281, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 21))
        self.menubar.setObjectName("menubar")
        self.menuReachmaster_GUI = QtWidgets.QMenu(self.menubar)
        self.menuReachmaster_GUI.setObjectName("menuReachmaster_GUI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuReachmaster_GUI.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def find_files_widget(self):
        """ Widget w/ directory paths, on close save the path (self.path = found_path).
            From that path, find video_files, behavior_times, classification_ids"""
        save_path = ''
        self.video_files = save_path + 'DLC_video.mp4'
        self.behavior_times = save_path + 'behavior_times.txt'
        self.classification_ids = save_path + 'class_ids.txt'

    def get_files_widget(self):
        """ Use paths to initialize, load data into widgets. """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Menu 2"))
        self.label_2.setText(_translate("MainWindow", "GUI Widgets"))
        self.label_3.setText(_translate("MainWindow", "Video Viewer"))
        self.menuReachmaster_GUI.setTitle(_translate("MainWindow", "Reachmaster GUI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
