# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage
import cv2
from cv2 import *
from functools import *
import numpy as np
from matplotlib import pyplot as plt
import src.openFileDialog as fd

from src.imageEditor import Ui_MainWindow
import src.imageEditor as ie


class MainWindow(QMainWindow,Ui_MainWindow, fd.FileDialog):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        fd.FileDialog.__init__(self)
        self.states = []
        self.cvImg= ''
        self.cvImg2 = ''
        self.add_menu_triggers()

    def open_file_settings(self):
        fname = fd.FileDialog.openFile(self, '', True, "", False)
        #print(fname)
        #fname = 'C:/Users/Caio/handExample.jpg'
        self.labelImage.setPixmap(QPixmap(fname))
        self.cvImg = cv2.imread(fname)
        self.cvImg2 = cv2.imread(fname, 0)

    def add_menu_triggers(self):
        self.actionOpenImage.triggered.connect(self.open_file_settings)
        self.actionThresholdBinary.triggered.connect(partial(self.threshold, 'bin'))
        self.actionThresholdBinaryInverse.triggered.connect(partial(self.threshold, 'bin_inv'))
        self.actionThresholdTruncate.triggered.connect(partial(self.threshold, 'trunc'))
        self.actionThresholdZero.triggered.connect(partial(self.threshold, 'zero'))
        self.actionThresholdZeroInverse.triggered.connect(partial(self.threshold, 'zero_inv'))
        self.actionThresholdAdaptativeGaussian.triggered.connect(partial(self.threshold, 'gau'))
        self.actionThresholdAdaptativeMean.triggered.connect(partial(self.threshold, 'med'))

    def threshold(self, type):

        #self.states.append(self.image)

        if type == 'bin':
            print(type)
            ret, thresh1 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_BINARY)
            #plt.imshow(thresh1)
            #plt.show()
            self.temp = thresh1
        elif type == 'bin_inv':
            print(type)
            ret, thresh2 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_BINARY_INV)
            self.temp = thresh2
        elif type == 'trunc':
            print(type)
            ret, thresh3 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_TRUNC)
            self.temp = thresh3
        elif type == 'zero':
            print(type)
            ret, thresh4 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_TOZERO)
            self.temp = thresh4
        elif type == 'zero_inv':
            print(type)
            ret, thresh5 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_TOZERO_INV)
            self.temp = thresh5
        elif type == 'gau':
            print(type)
            img = cv2.medianBlur(self.cvImg2, 5)
            ret, th1 = cv2.threshold(self.cvImg2, 127, 255, cv2.THRESH_BINARY)
            th2 = cv2.adaptiveThreshold(self.cvImg2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                        cv2.THRESH_BINARY, 11, 2)
            self.displayImageGray(th2)
            return
        elif type == 'med':
            print(type)
            img = cv2.medianBlur(self.cvImg2, 5)
            ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            th3 = cv2.adaptiveThreshold(th1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                        cv2.THRESH_BINARY, 11, 2)

            self.displayImageGray(th3)
            return


            #height, width , shape = self.cvImg.shape
        #print(self.cvImg.shape)
        #print(height, width)
        #bytesPerLine = 3 * width
        #print(bytesPerLine)
        #qImg = QImage(self.cvImg.data, width, height, bytesPerLine + 1, QImage.Format_RGB888)

        #self.image.setPixmap(qImg)

        self.displayImage()

    def displayImageGray(self, th):
        if len(th.shape) < 3 or th.shape[2] == 1:
            image = cv2.cvtColor(th, cv2.COLOR_GRAY2RGB)
        else:
            image = cv2.cvtColor(th, cv2.COLOR_BGR2RGB)

        height, width, byteValue = image.shape
        byteValue = byteValue * width

        qimage = QImage(image, width, height, byteValue, QImage.Format_RGB888)

        self.labelImage.setPixmap(QPixmap.fromImage(qimage))

        #self.states.append(self.labelImage)

        return

    def displayImage(self):
        qformat = QImage.Format_Indexed8
        if len(self.temp.shape) == 3:
            if self.temp.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
            img = QImage(self.temp.data,
                               self.temp.shape[1],
                               self.temp.shape[0],
                               self.temp.strides[0],  # <--- +++
                               qformat)
            #img = img.rgbSwapped()
            self.labelImage.setPixmap(QPixmap.fromImage(img))
            self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
            print("displayed")
            self.states.append(self.labelImage)
        else:
            print(self.temp.shape)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())