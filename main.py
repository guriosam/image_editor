# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2
from cv2 import *
from functools import *
import numpy as np
from matplotlib import pyplot as plt
import src.fileDialog as fd

from src.imageEditor import Ui_MainWindow
import src.imageEditor as ie


class MainWindow(QMainWindow,Ui_MainWindow, fd.FileDialog):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        fd.FileDialog.__init__(self)
        self.states = []
        self.appliedFilters = []
        self.cvImg = ''
        self.cvImg2 = ''
        self.addMenuTriggers()
        self.fname = ''

    def resizeEvent(self, event):
        if self.cvImg is '':
            pass

        size = self.labelImage.size()
        pixmap = QPixmap(self.fname)
        pixmap = pixmap.scaled(size, Qt.KeepAspectRatio)
        self.labelImage.setPixmap(pixmap)

    def openFileSettings(self):
        self.fname = fd.FileDialog.openFile(self, '', True, "", False)
        pixmap = QPixmap(self.fname)

        pixmap = pixmap.scaled(self.labelImage.size(), Qt.KeepAspectRatio)
        self.labelImage.setPixmap(pixmap)

        self.cvImg = cv2.imread(self.fname, 0)
        self.cvImg2 = cv2.imread(self.fname)

    def saveFileSettings(self):
        filepath = fd.FileDialog.saveFile(self, '', True)

        if filepath[0] is '':
            return

        self.labelImage.pixmap().toImage().save(filepath[0] + '.jpg')

    def addMenuTriggers(self):
        self.actionOpenImage.triggered.connect(self.openFileSettings)
        self.actionSaveImage.triggered.connect(self.saveFileSettings)
        self.actionThresholdBinary.triggered.connect(partial(self.threshold, 'bin'))
        self.actionThresholdBinaryInverse.triggered.connect(partial(self.threshold, 'bin_inv'))
        self.actionThresholdTruncate.triggered.connect(partial(self.threshold, 'trunc'))
        self.actionThresholdZero.triggered.connect(partial(self.threshold, 'zero'))
        self.actionThresholdZeroInverse.triggered.connect(partial(self.threshold, 'zero_inv'))
        self.actionThresholdAdaptativeGaussian.triggered.connect(partial(self.threshold, 'gau'))
        self.actionThresholdAdaptativeMean.triggered.connect(partial(self.threshold, 'med'))
        self.actionFeatureTracking.triggered.connect(self.featureTracking)
        self.listWidgetActionQueue.itemClicked.connect(self.itemClicked)

    def itemClicked(self, item):
        print(item.text())
        index = self.listWidgetActionQueue.row(item)
        self.labelImage = self.states[index]

    def featureTracking(self):
       # gray = cv2.cvtColor(self.cvImg, 0)

        corners = cv2.goodFeaturesToTrack(self.cvImg, 25, 0.01, 10)
        corners = np.int0(corners)

        self.temp = self.cvImg

        for i in corners:
            x, y = i.ravel()
            cv2.circle(self.temp, (x, y), 3, 255, -1)


        self.displayImageGray()
        # self.displayImage()

    def threshold(self, type):

        if isinstance(self.cvImg, str):
            return

        self.listWidgetActionQueue.addItem(type)

        if type == 'bin':
            ret, thresh1 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_BINARY)
            self.temp = thresh1
        elif type == 'bin_inv':
            ret, thresh2 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_BINARY_INV)
            self.temp = thresh2
        elif type == 'trunc':
            ret, thresh3 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_TRUNC)
            self.temp = thresh3
        elif type == 'zero':
            ret, thresh4 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_TOZERO)
            self.temp = thresh4
        elif type == 'zero_inv':
            ret, thresh5 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_TOZERO_INV)
            self.temp = thresh5
        elif type == 'gau':
            img = cv2.medianBlur(self.cvImg, 5)
            ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            th2 = cv2.adaptiveThreshold(th1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                        cv2.THRESH_BINARY, 11, 2)
            self.temp = th2
        elif type == 'med':
            img = cv2.medianBlur(self.cvImg, 5)
            ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            th3 = cv2.adaptiveThreshold(th1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                        cv2.THRESH_BINARY, 11, 2)
            self.temp = th3

        if len(self.temp.shape) < 3 or self.temp.shape[2] == 1:
            self.displayImageGray()
        elif len(self.temp.shape) == 3:
            self.displayImage()

    def displayImageGray(self, ):
        if len(self.temp.shape) < 3 or self.temp.shape[2] == 1:
            image = cv2.cvtColor(self.temp, cv2.COLOR_GRAY2RGB)
        else:
            image = cv2.cvtColor(self.temp, cv2.COLOR_BGR2RGB)

        height, width, byteValue = image.shape
        byteValue = byteValue * width

        qimage = QImage(image, width, height, byteValue, QImage.Format_RGB888)

        self.labelImage.setPixmap(QPixmap.fromImage(qimage))
        # self.labelImage.pixmap().scaled(width, height, QtCore.Qt.KeepAspectRatio)

        # self.states.append(self.labelImage)

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

            #img.scaled(self.labelImage.size(),Qt.KeepAspectRatio)
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
