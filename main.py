
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1121, 771))
        self.tabWidget.setObjectName("tabWidget")
        self.inputTab = QtWidgets.QWidget()
        self.inputTab.setObjectName("inputTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 271, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.imgLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.imgLayout1.setContentsMargins(0, 0, 0, 0)
        self.imgLayout1.setObjectName("imgLayout1")
        self.label = QtWidgets.QLabel(self.inputTab)
        self.label.setGeometry(QtCore.QRect(0, 0, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.inputTab)
        self.label_2.setGeometry(QtCore.QRect(570, 0, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.inputTab)
        self.label_3.setGeometry(QtCore.QRect(0, 290, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.inputTab)
        self.label_4.setGeometry(QtCore.QRect(570, 290, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.inputTab)
        self.label_5.setGeometry(QtCore.QRect(0, 260, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setObjectName("label_5")
        self.componentSlider1 = QtWidgets.QSlider(self.inputTab)
        self.componentSlider1.setGeometry(QtCore.QRect(130, 260, 351, 22))
        self.componentSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.componentSlider1.setObjectName("componentSlider1")
        self.lcdNumber = QtWidgets.QLCDNumber(self.inputTab)
        self.lcdNumber.setGeometry(QtCore.QRect(490, 260, 51, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_6 = QtWidgets.QLabel(self.inputTab)
        self.label_6.setGeometry(QtCore.QRect(570, 260, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.inputTab)
        self.lcdNumber_2.setGeometry(QtCore.QRect(1060, 260, 51, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.componentSlider2 = QtWidgets.QSlider(self.inputTab)
        self.componentSlider2.setGeometry(QtCore.QRect(700, 260, 351, 22))
        self.componentSlider2.setOrientation(QtCore.Qt.Horizontal)
        self.componentSlider2.setObjectName("componentSlider2")
        self.label_7 = QtWidgets.QLabel(self.inputTab)
        self.label_7.setGeometry(QtCore.QRect(0, 550, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setObjectName("label_7")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.inputTab)
        self.lcdNumber_3.setGeometry(QtCore.QRect(490, 550, 51, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.componentSlider3 = QtWidgets.QSlider(self.inputTab)
        self.componentSlider3.setGeometry(QtCore.QRect(130, 550, 351, 22))
        self.componentSlider3.setOrientation(QtCore.Qt.Horizontal)
        self.componentSlider3.setObjectName("componentSlider3")
        self.label_8 = QtWidgets.QLabel(self.inputTab)
        self.label_8.setGeometry(QtCore.QRect(570, 550, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setObjectName("label_8")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.inputTab)
        self.lcdNumber_4.setGeometry(QtCore.QRect(1060, 550, 51, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.componentSlider4 = QtWidgets.QSlider(self.inputTab)
        self.componentSlider4.setGeometry(QtCore.QRect(700, 550, 351, 22))
        self.componentSlider4.setOrientation(QtCore.Qt.Horizontal)
        self.componentSlider4.setObjectName("componentSlider4")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(290, 30, 241, 221))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.componentLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.componentLayout1.setContentsMargins(0, 0, 0, 0)
        self.componentLayout1.setObjectName("componentLayout1")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(570, 30, 271, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.imgLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.imgLayout2.setContentsMargins(0, 0, 0, 0)
        self.imgLayout2.setObjectName("imgLayout2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 320, 271, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.imgLayout3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.imgLayout3.setContentsMargins(0, 0, 0, 0)
        self.imgLayout3.setObjectName("imgLayout3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(570, 320, 271, 221))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.imgLayout4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.imgLayout4.setContentsMargins(0, 0, 0, 0)
        self.imgLayout4.setObjectName("imgLayout4")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(860, 30, 241, 221))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.componentLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.componentLayout2.setContentsMargins(0, 0, 0, 0)
        self.componentLayout2.setObjectName("componentLayout2")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(290, 320, 241, 221))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.componentLayout3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.componentLayout3.setContentsMargins(0, 0, 0, 0)
        self.componentLayout3.setObjectName("componentLayout3")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(860, 320, 241, 221))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.componentLayout4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.componentLayout4.setContentsMargins(0, 0, 0, 0)
        self.componentLayout4.setObjectName("componentLayout4")
        self.comboBox1 = QtWidgets.QComboBox(self.inputTab)
        self.comboBox1.setGeometry(QtCore.QRect(60, 0, 231, 22))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.line = QtWidgets.QFrame(self.inputTab)
        self.line.setGeometry(QtCore.QRect(0, 280, 1121, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.inputTab)
        self.line_2.setGeometry(QtCore.QRect(540, -20, 20, 771))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.inputTab)
        self.line_3.setGeometry(QtCore.QRect(0, 570, 1121, 21))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.label_9 = QtWidgets.QLabel(self.inputTab)
        self.label_9.setGeometry(QtCore.QRect(70, 600, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.mixingComboBox = QtWidgets.QComboBox(self.inputTab)
        self.mixingComboBox.setGeometry(QtCore.QRect(240, 600, 191, 22))
        self.mixingComboBox.setObjectName("mixingComboBox")
        self.mixingComboBox.addItem("")
        self.mixingComboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.inputTab)
        self.label_10.setGeometry(QtCore.QRect(70, 650, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.outerRadioButton = QtWidgets.QRadioButton(self.inputTab)
        self.outerRadioButton.setGeometry(QtCore.QRect(210, 650, 95, 20))
        self.outerRadioButton.setObjectName("outerRadioButton")
        self.innerRadioButton = QtWidgets.QRadioButton(self.inputTab)
        self.innerRadioButton.setGeometry(QtCore.QRect(350, 650, 95, 20))
        self.innerRadioButton.setObjectName("innerRadioButton")
        self.label_11 = QtWidgets.QLabel(self.inputTab)
        self.label_11.setGeometry(QtCore.QRect(610, 650, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.windowRadioButton1 = QtWidgets.QRadioButton(self.inputTab)
        self.windowRadioButton1.setGeometry(QtCore.QRect(750, 650, 95, 20))
        self.windowRadioButton1.setObjectName("windowRadioButton1")
        self.windowRadioButton2 = QtWidgets.QRadioButton(self.inputTab)
        self.windowRadioButton2.setGeometry(QtCore.QRect(880, 650, 95, 20))
        self.windowRadioButton2.setObjectName("windowRadioButton2")
        self.label_14 = QtWidgets.QLabel(self.inputTab)
        self.label_14.setGeometry(QtCore.QRect(70, 700, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.comboBox2 = QtWidgets.QComboBox(self.inputTab)
        self.comboBox2.setGeometry(QtCore.QRect(630, 0, 231, 22))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox3 = QtWidgets.QComboBox(self.inputTab)
        self.comboBox3.setGeometry(QtCore.QRect(60, 290, 231, 22))
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox4 = QtWidgets.QComboBox(self.inputTab)
        self.comboBox4.setGeometry(QtCore.QRect(630, 290, 231, 22))
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.regionSizeSlide = QtWidgets.QSlider(self.inputTab)
        self.regionSizeSlide.setGeometry(QtCore.QRect(180, 700, 291, 22))
        self.regionSizeSlide.setOrientation(QtCore.Qt.Horizontal)
        self.regionSizeSlide.setObjectName("regionSizeSlide")
        self.tabWidget.addTab(self.inputTab, "")
        self.outputTab = QtWidgets.QWidget()
        self.outputTab.setObjectName("outputTab")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.outputTab)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 50, 531, 521))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.windowLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.windowLayout1.setContentsMargins(0, 0, 0, 0)
        self.windowLayout1.setObjectName("windowLayout1")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.outputTab)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(550, 50, 561, 521))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.windowLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.windowLayout2.setContentsMargins(0, 0, 0, 0)
        self.windowLayout2.setObjectName("windowLayout2")
        self.label_12 = QtWidgets.QLabel(self.outputTab)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.outputTab)
        self.label_13.setGeometry(QtCore.QRect(560, 10, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.outputTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Image 1"))
        self.label_2.setText(_translate("MainWindow", "Image 2"))
        self.label_3.setText(_translate("MainWindow", "Image 3"))
        self.label_4.setText(_translate("MainWindow", "Image 4"))
        self.label_5.setText(_translate("MainWindow", "Component Value:"))
        self.label_6.setText(_translate("MainWindow", "Component Value:"))
        self.label_7.setText(_translate("MainWindow", "Component Value:"))
        self.label_8.setText(_translate("MainWindow", "Component Value:"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Phase"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "Real"))
        self.comboBox1.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.label_9.setText(_translate("MainWindow", "Mixing Type:"))
        self.mixingComboBox.setItemText(0, _translate("MainWindow", "Component"))
        self.mixingComboBox.setItemText(1, _translate("MainWindow", "Region"))
        self.label_10.setText(_translate("MainWindow", "Region:"))
        self.outerRadioButton.setText(_translate("MainWindow", "Outer"))
        self.innerRadioButton.setText(_translate("MainWindow", "Inner"))
        self.label_11.setText(_translate("MainWindow", "Output Window :"))
        self.windowRadioButton1.setText(_translate("MainWindow", "Window 1"))
        self.windowRadioButton2.setText(_translate("MainWindow", "Window 2"))
        self.label_14.setText(_translate("MainWindow", "Region Size:"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "Phase"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "Real"))
        self.comboBox2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.comboBox3.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.comboBox3.setItemText(1, _translate("MainWindow", "Phase"))
        self.comboBox3.setItemText(2, _translate("MainWindow", "Real"))
        self.comboBox3.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.comboBox4.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.comboBox4.setItemText(1, _translate("MainWindow", "Phase"))
        self.comboBox4.setItemText(2, _translate("MainWindow", "Real"))
        self.comboBox4.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inputTab), _translate("MainWindow", "Input"))
        self.label_12.setText(_translate("MainWindow", "Window 1"))
        self.label_13.setText(_translate("MainWindow", "Window 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.outputTab), _translate("MainWindow", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())