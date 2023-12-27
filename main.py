from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QObject
from imageviewer import  ImageViewer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QVBoxLayout, QPushButton, QWidget
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap as qtg

import matplotlib.pyplot as plt
from PIL import Image as PILImage
import cv2
import numpy as np
import threading
import time

class CustomLabel(QLabel):
    doubleClicked = pyqtSignal()
    move_signal = pyqtSignal(int, int)
    
    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
        self.setMouseTracking(True)
        self.origin = None
        self.x=0
        self.y=0
        
    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()
        super(CustomLabel, self).mouseDoubleClickEvent(event)


    def mousePressEvent(self, event):
            self.origin = event.pos()


    def mouseMoveEvent(self, event):
        global x
        global y
        
        if self.origin:
            delta = event.pos() - self.origin
            if delta.x()>0:
                self.x+=1
            elif delta.x()<0:
                self.x-=1
            elif delta.y()<0:
                self.y+=2
            elif delta.y()>0:
                self.y-=2
            self.origin = event.pos()
            self.move_signal.emit(self.x, self.y)
            

    def mouseReleaseEvent(self, event):
        self.origin = None
        self.x = 0
        self.y = 0
        self.move_signal.emit(self.x, self.y)
        # You can add additional logic here if neededs

    def contains_image(self):
        return not self.pixmap().isNull() if self.pixmap() else False

    def remove_image(self):
        self.clear()



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
        # self.verticalLayoutWidget = QtWidgets.QWidget(self.inputTab)
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 271, 221))
        # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # self.verticalLayoutWidget.setStyleSheet("background-color: lightblue;")
        self.createImageLayouts()
        self.imgLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.imgLayout1.setContentsMargins(0, 0, 0, 0)
        self.imgLayout1.setObjectName("imgLayout1")
        self.imgLayout1.addWidget(self.img_label1)
        
        

        # Set background color for the verticalLayoutWidget
        
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
        
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.inputTab)
        self.lcdNumber_1.setGeometry(QtCore.QRect(490, 260, 51, 23))
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.lcdNumber_1.display(100)
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
        self.lcdNumber_2.display(100)
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
        self.lcdNumber_3.display(100)
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
        self.lcdNumber_4.display(100)
        
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
        self.componentLayout1.addWidget(self.component_label1)
        self.imgLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.imgLayout2.setContentsMargins(0, 0, 0, 0)
        self.imgLayout2.setObjectName("imgLayout2")
        self.imgLayout2.addWidget(self.img_label2)
        self.imgLayout3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.imgLayout3.setContentsMargins(0, 0, 0, 0)
        self.imgLayout3.setObjectName("imgLayout3")
        self.imgLayout3.addWidget(self.img_label3)
        self.imgLayout4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.imgLayout4.setContentsMargins(0, 0, 0, 0)
        self.imgLayout4.setObjectName("imgLayout4")
        self.imgLayout4.addWidget(self.img_label4)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(860, 30, 241, 221))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.componentLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.componentLayout2.setContentsMargins(0, 0, 0, 0)
        self.componentLayout2.setObjectName("componentLayout2")
        self.componentLayout2.addWidget(self.component_label2)
        
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(290, 320, 241, 221))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.componentLayout3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.componentLayout3.setContentsMargins(0, 0, 0, 0)
        self.componentLayout3.setObjectName("componentLayout3")
        self.componentLayout3.addWidget(self.component_label3)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(860, 320, 241, 221))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.componentLayout4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.componentLayout4.setContentsMargins(0, 0, 0, 0)
        self.componentLayout4.setObjectName("componentLayout4")
        self.componentLayout4.addWidget(self.component_label4)
        self.comboBox1 = QtWidgets.QComboBox(self.inputTab)
        self.comboBox1.setGeometry(QtCore.QRect(60, 0, 231, 22))
        self.comboBox1.setObjectName("comboBox1")
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
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        
        
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
        self.comboBox3 = QtWidgets.QComboBox(self.inputTab)
        self.comboBox3.setGeometry(QtCore.QRect(60, 290, 231, 22))
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")

        self.comboBox4 = QtWidgets.QComboBox(self.inputTab)
        self.comboBox4.setGeometry(QtCore.QRect(630, 290, 231, 22))
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")

        self.regionSizeSlide = QtWidgets.QSlider(self.inputTab)
        self.regionSizeSlide.setGeometry(QtCore.QRect(180, 700, 291, 22))
        self.regionSizeSlide.setOrientation(QtCore.Qt.Horizontal)
        self.regionSizeSlide.setObjectName("regionSizeSlide")
        self.regionSizeSlide.setRange(0,100)

        self.tabWidget.addTab(self.inputTab, "")
        self.outputTab = QtWidgets.QWidget()
        self.outputTab.setObjectName("outputTab")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.outputTab)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 50, 531, 521))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.windowLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.windowLayout1.setContentsMargins(0, 0, 0, 0)
        self.windowLayout1.setObjectName("windowLayout1")
        self.windowLayout1.addWidget(self.output_label1)

        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.outputTab)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(550, 50, 561, 521))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.windowLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.windowLayout2.setContentsMargins(0, 0, 0, 0)
        self.windowLayout2.setObjectName("windowLayout2")
        self.windowLayout2.addWidget(self.output_label2)
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
        self.label_11 = QtWidgets.QLabel(self.outputTab)
        self.label_11.setGeometry(QtCore.QRect(300, 650, 121, 16))
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.windowRadioButton1 = QtWidgets.QRadioButton(self.outputTab)
        self.windowRadioButton1.setGeometry(QtCore.QRect(450, 650, 95, 20))
        self.windowRadioButton1.setObjectName("windowRadioButton1")
        self.windowRadioButton2 = QtWidgets.QRadioButton(self.outputTab)
        self.windowRadioButton2.setGeometry(QtCore.QRect(600, 650, 95, 20))
        self.windowRadioButton2.setObjectName("windowRadioButton2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.currentmode = 0
        self.thereisimage = False

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mixingComboBox.currentIndexChanged.connect(lambda index: self.changemode(index))
        self.images={
            '':'',
            'image1':None,
            'image2':None,
            'image3':None,
            'image4':None,

        }

        self.mixingdata ={
         'image1':{
            '':'',
            'Magnitude':0,
            'Phase':0,
            'Real':0,
            'Imaginary':0,
            'RatioReal':1,
            'RatioImaginary':1,
            'RatioPhase':1,
            'RatioMagnitude':1,

        },
        'image2':{
            '':'',
            'Magnitude':0,
            'Phase':0,
            'Real':0,
            'Imaginary':0,
            'RatioReal':1,
            'RatioImaginary':1,
            'RatioPhase':1,
            'RatioMagnitude':1,
        },
        'image3':{
            '':'',
            'Magnitude':0,
            'Phase':0,
            'Real':0,
            'Imaginary':0,
            'RatioReal':1,
            'RatioImaginary':1,
            'RatioPhase':1,
            'RatioMagnitude':1,
        },
        'image4':{
            '':'',
            '':'',
            'Magnitude':0,
            'Phase':0,
            'Real':0,
            'Imaginary':0,
            'RatioReal':1,
            'RatioImaginary':1,
            'RatioPhase':1,
            'RatioMagnitude':1,
        },

        }
        for i in range(1,5):
          slidername = f"componentSlider{i}"
          slider = getattr(self, slidername, None)
          slider.setRange(0,100)
          slider.setValue(100)
          slider.valueChanged.connect(lambda value, range=i: self.adjustratio(value, range))
        
        
        
        self.regionSizeSlide.valueChanged.connect(lambda value: self.regionslice(value))
        
        self.windowRadioButton1.clicked.connect(self.on_windowRadioButton_clicked)
        self.windowRadioButton2.clicked.connect(self.on_windowRadioButton_clicked)

    
    def regionslice(self,value):
        if  (not self.outerRadioButton.isChecked()) and (not self.innerRadioButton.isChecked()):
            return
        
        if self.innerRadioButton.isChecked():
            for i in range(1,5):
                imagename = f"image{i}"
                if self.images[imagename] != None:
                    self.images[imagename].regionsliceinner(value,self.currentmode)
                    if self.currentmode==0:
                        self.mixingdata[imagename]["Real"] = self.images[imagename].getcomponents("Real")
                        self.mixingdata[imagename]["Imaginary"] = self.images[imagename].getcomponents("Imaginary")
                    else:
                        self.mixingdata[imagename]["Magnitude"] = self.images[imagename].getcomponents("Magnitude")
                        self.mixingdata[imagename]["Phase"] = self.images[imagename].getcomponents("Phase")
                    
                    self.recover_image()
                
        elif self.outerRadioButton.isChecked():
               for i in range(1,5):
                imagename = f"image{i}"
                if self.images[imagename] != None:
                    self.images[imagename].regionsliceouter(value,self.currentmode)
                    if self.currentmode ==0:
                        self.mixingdata[imagename]["Real"] = self.images[imagename].getcomponents("Real")
                        self.mixingdata[imagename]["Imaginary"] = self.images[imagename].getcomponents("Imaginary")
                    else:
                        self.mixingdata[imagename]["Magnitude"] = self.images[imagename].getcomponents("Magnitude")
                        self.mixingdata[imagename]["Phase"] = self.images[imagename].getcomponents("Phase")
                    self.recover_image()

    
                   
            
        
            

        
        

    def on_windowRadioButton_clicked(self):
        # This method will be called when windowRadioButton1 is clicked
        if self.windowRadioButton1.isChecked():
            self.output_label2.remove_image()
            if self.thereisimage:
               self.recover_image()
        elif self.windowRadioButton2.isChecked():
            self.output_label1.remove_image()
            if self.thereisimage:
               self.recover_image()

            


    def adjustratio(self, value, range):
        
        lcd = f"lcdNumber_{range}"
        lcdnumber = getattr(self, lcd, None)
        lcdnumber.display(value)
        image = f"image{range}"
        comboBox = f"comboBox{range}"
        comboBox_instance = getattr(self, comboBox, None)
        componentname = comboBox_instance.currentText()
        ratio = f"Ratio{componentname}"
        self.mixingdata[image][ratio]=value/100
        if self.thereisimage:
          self.recover_image()
        



    def changemode(self, index):   
        for i in range(1, 5):
            self.currentmode = index
            comboBox = f"comboBox{i}"
            comboBox_instance = getattr(self, comboBox, None)
            if index ==0:
                comboBox_instance.setItemText(0, "Real")
                comboBox_instance.setItemText(1,  "Imaginary")
            else:
                comboBox_instance.setItemText(0, "Magnitude")
                comboBox_instance.setItemText(1,  "Phase")


            




    def process_inner_region(self, component, region_percent):
        # Calculate the size of the inner rectangle based on the given percentage
        region_size = int(min(component.size) * region_percent / 100)
        
        # Calculate the coordinates of the rectangle
        start_x = (component.size[1] - region_size) // 2
        start_y = (component.size[0] - region_size) // 2
        end_x = start_x + region_size
        end_y = start_y + region_size

        # Create an array of zeros with the same shape as the component
        processed_component = np.zeros_like(component)

        # Set the values in the selected region to 1
        processed_component[start_y:end_y, start_x:end_x] = 1

        plt.imshow(processed_component, cmap='gray')
        plt.title(f'{component} Component')
        plt.show()
        
    


    def createImageLayouts(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 271, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayoutWidget_2 =QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(570, 30, 271, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 320, 271, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.inputTab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(570, 320, 271, 221))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
         
        self.img_label1 = CustomLabel() 
        self.img_label2 = CustomLabel() 
        self.img_label3 = CustomLabel() 
        self.img_label4 = CustomLabel() 

        self.component_label1 = CustomLabel() 
        self.component_label2 = CustomLabel() 
        self.component_label3 = CustomLabel() 
        self.component_label4 = CustomLabel() 

        self.output_label1 = CustomLabel()
        self.output_label2 = CustomLabel()

        
        # Set background color for the verticalLayoutWidget
        

        # Connect the doubleClicked signal to onDoubleClic

        self.img_label1.doubleClicked.connect(lambda: self.onDoubleClick(1))
        self.img_label2.doubleClicked.connect(lambda: self.onDoubleClick(2))
        self.img_label3.doubleClicked.connect(lambda: self.onDoubleClick(3))
        self.img_label4.doubleClicked.connect(lambda: self.onDoubleClick(4))

    def onDoubleClick(self,index):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.xpm *.jpg *.bmp *.gif)", options=options)
        if image_path:

            labelname1 = f"img_label{index}"
            imagelabel1 = getattr(self, labelname1, None)
            labelname2 = f"component_label{index}"
            imagelabel2 = getattr(self, labelname2, None)

            image =ImageViewer(imagelabel1,imagelabel2,image_path)
            imagename = f"image{index}"
            self.mixingdata[imagename]["Magnitude"] = image.getorgcomponents("Magnitude")
            self.mixingdata[imagename]["Phase"] = image.getorgcomponents("Phase")
            self.mixingdata[imagename]["Real"] = image.getorgcomponents("Real")
            self.mixingdata[imagename]["Imaginary"] = image.getorgcomponents("Imaginary")
            self.images[imagename] = image
            
            
            comboBox = f"comboBox{index}"
            comboBox_instance = getattr(self, comboBox, None)
            image.show_ft_component(comboBox_instance.currentText())
            comboBox_instance.currentIndexChanged.connect(lambda index: image.show_ft_component(comboBox_instance.currentText()))
            
            imagelabel1.move_signal.connect(lambda x, y: image.adjust_brightness_contrast(x, y))
            self.thereisimage = True
            self.recover_image()

    def recover_image(self):
        if self.windowRadioButton1.isChecked() or self.windowRadioButton2.isChecked(): 
            # Assuming componentsimage is a NumPy array
            if self.currentmode == 0:
                component1 =self.mixingdata["image1"]["Real"]*self.mixingdata["image1"]["RatioReal"] + 1j * self.mixingdata["image1"]["Imaginary"]*self.mixingdata["image1"]["RatioImaginary"]
                component2 =self.mixingdata["image2"]["Real"]*self.mixingdata["image2"]["RatioReal"] + 1j * self.mixingdata["image2"]["Imaginary"]*self.mixingdata["image2"]["RatioImaginary"]
                component3 =self.mixingdata["image3"]["Real"]*self.mixingdata["image3"]["RatioReal"] + 1j * self.mixingdata["image3"]["Imaginary"]*self.mixingdata["image3"]["RatioImaginary"]
                component4 =self.mixingdata["image4"]["Real"]*self.mixingdata["image4"]["RatioReal"] + 1j * self.mixingdata["image4"]["Imaginary"]*self.mixingdata["image4"]["RatioImaginary"]
                
            else:
                component1 =(self.mixingdata["image1"]["Magnitude"]*self.mixingdata["image1"]["RatioMagnitude"]) * np.exp(1j * self.mixingdata["image1"]["Phase"]*self.mixingdata["image1"]["RatioPhase"])
                component2 =(self.mixingdata["image2"]["Magnitude"]*self.mixingdata["image2"]["RatioMagnitude"]) * np.exp(1j * self.mixingdata["image2"]["Phase"]*self.mixingdata["image2"]["RatioPhase"])
                component3 =(self.mixingdata["image3"]["Magnitude"]*self.mixingdata["image3"]["RatioMagnitude"]) * np.exp(1j * self.mixingdata["image3"]["Phase"]*self.mixingdata["image3"]["RatioPhase"])
                component4 =(self.mixingdata["image4"]["Magnitude"]*self.mixingdata["image4"]["RatioMagnitude"]) * np.exp(1j * self.mixingdata["image4"]["Phase"]*self.mixingdata["image4"]["RatioPhase"])

            complex_array = component1+component2+component3+component4
            # Perform inverse 2D Fourier Transform
            f_transform_inverse = np.fft.ifft2(np.fft.ifftshift(complex_array))

            # Take the real part to get the recovered image
            componentsimage = np.real(f_transform_inverse)
            recovered_image = (componentsimage - np.min(componentsimage)) / (np.max(componentsimage) - np.min(componentsimage))
            recovered_image = (recovered_image * 255).astype(np.uint8)

            # Resize the image
            resized_image = cv2.resize(recovered_image, (271*2, 221*2))

            # Convert the NumPy array to a QImage
            height, width = resized_image.shape
            qt_image = QtGui.QImage(resized_image.data, width, height, width, QtGui.QImage.Format_Grayscale8)

            # Convert QImage to QPixmap
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            if self.windowRadioButton1.isChecked():
                # Assuming self.ft_label is a QLabel where you want to display the recovered image
                self.output_label1.setPixmap(pixmap)  
            elif self.windowRadioButton2.isChecked(): 
                self.output_label2.setPixmap(pixmap)  
        
        
    


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
        self.comboBox1.setItemText(0, _translate("MainWindow", "Real"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Imaginary"))
        self.label_9.setText(_translate("MainWindow", "Mixing Type:"))
        self.mixingComboBox.setItemText(0, _translate("MainWindow", "real-imag"))
        self.mixingComboBox.setItemText(1, _translate("MainWindow", "mag-phase"))
        self.label_10.setText(_translate("MainWindow", "Region:"))
        self.outerRadioButton.setText(_translate("MainWindow", "Outer"))
        self.innerRadioButton.setText(_translate("MainWindow", "Inner"))

        self.label_11.setText(_translate("MainWindow", "Output Window :"))
        self.windowRadioButton1.setText(_translate("MainWindow", "Window 1"))
        self.windowRadioButton2.setText(_translate("MainWindow", "Window 2"))
        self.label_14.setText(_translate("MainWindow", "Region Size:"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "Real"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "Imaginary"))
        self.comboBox3.setItemText(0, _translate("MainWindow", "Real"))
        self.comboBox3.setItemText(1, _translate("MainWindow", "Imaginary"))
        self.comboBox4.setItemText(0, _translate("MainWindow", "Real"))
        self.comboBox4.setItemText(1, _translate("MainWindow", "Imaginary"))
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
