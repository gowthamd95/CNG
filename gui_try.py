from PyQt5 import QtCore, QtGui, QtWidgets
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.qCircularBar = QCircularBar(self.centralwidget)
        self.qCircularBar.setGeometry(QtCore.QRect(50, 20, 231, 231))
        self.qCircularBar.setProperty("value", 63.0)
        self.qCircularBar.setMinValue(0.0)
        self.qCircularBar.setMaxValue(100.0)
        self.qCircularBar.setThreshold(80.0)
        self.qCircularBar.setUnits("")
        self.qCircularBar.setStartAngle(210)
        self.qCircularBar.setEndAngle(-30)
        self.qCircularBar.setProperty("enableThreshold", True)
        self.qCircularBar.setProperty("enableNumericIndicator", True)
        self.qCircularBar.setObjectName("qCircularBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.qCircularBar.setToolTip(_translate("MainWindow", "Meter"))
        self.qCircularBar.setWhatsThis(_translate("MainWindow", "Meter widget"))
        self.qCircularBar.setLabel(_translate("MainWindow", "VOL"))
 
from qcircularbar import QCircularBar
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())