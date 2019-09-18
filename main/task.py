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
import filedialog as fd


class Ui_MainWindow(object):

    states = []

    def open_file_settings(self):
        fname = fd.FileDialog("", True, "", False)
        #print(fname)
        #fname = 'C:/Users/Caio/handExample.jpg'
        self.image.setPixmap(QPixmap(fname))
        self.cvImg = cv2.imread(fname, cv2.IMREAD_COLOR)
        self.cvImg2 = cv2.imread(fname, 0)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 791, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.image.setText("")
        self.image.setObjectName("image")
        self.verticalLayout_2.addWidget(self.image)
        self.list_actions = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list_actions.setMaximumSize(QtCore.QSize(16777215, 50))
        self.list_actions.setObjectName("list_actions")
        self.verticalLayout_2.addWidget(self.list_actions)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuFiltros = QtWidgets.QMenu(self.menubar)
        self.menuFiltros.setObjectName("menuFiltros")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_image = QtWidgets.QAction(MainWindow)
        self.open_image.setObjectName("open_image")
        self.save_image = QtWidgets.QAction(MainWindow)
        self.save_image.setObjectName("save_image")
        self.close = QtWidgets.QAction(MainWindow)
        self.close.setObjectName("close")
        self.action_bin = QtWidgets.QAction(MainWindow)
        self.action_bin.setObjectName("action_bin")
        self.action_bin_inv = QtWidgets.QAction(MainWindow)
        self.action_bin_inv.setObjectName("action_bin_inv")
        self.action_trunc = QtWidgets.QAction(MainWindow)
        self.action_trunc.setObjectName("action_trunc")
        self.action_zero = QtWidgets.QAction(MainWindow)
        self.action_zero.setObjectName("action_zero")
        self.action_zero_inv = QtWidgets.QAction(MainWindow)
        self.action_zero_inv.setObjectName("action_zero_inv")
        self.action_adap_gau = QtWidgets.QAction(MainWindow)
        self.action_adap_gau.setObjectName("action_adap_gau")
        self.action_adap_med = QtWidgets.QAction(MainWindow)
        self.action_adap_med.setObjectName("action_adap_med")
        self.menuArquivo.addAction(self.open_image)
        self.menuArquivo.addAction(self.save_image)
        self.menuArquivo.addAction(self.close)
        self.menuFiltros.addAction(self.action_bin)
        self.menuFiltros.addAction(self.action_bin_inv)
        self.menuFiltros.addAction(self.action_trunc)
        self.menuFiltros.addAction(self.action_zero)
        self.menuFiltros.addAction(self.action_zero_inv)
        self.menuFiltros.addAction(self.action_adap_gau)
        self.menuFiltros.addAction(self.action_adap_med)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuFiltros.menuAction())

        self.retranslateUi(MainWindow)
        self.list_actions.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def threshold(self, type):

        self.states.append(self.image)

        if type == 'bin':
            print(type)
            ret, thresh1 = cv2.threshold(self.cvImg, 127, 255, cv2.THRESH_BINARY)
            plt.imshow(thresh1)
            plt.show()
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

        self.image.setPixmap(QPixmap.fromImage(qimage))

        self.states.append(self.image)

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
            self.image.setPixmap(QPixmap.fromImage(img))
            self.image.setAlignment(QtCore.Qt.AlignCenter)
            print("displayed")
            self.states.append(self.image)
        else:
            print(self.temp.shape)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.list_actions.setSortingEnabled(True)
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuFiltros.setTitle(_translate("MainWindow", "Filtros"))
        self.open_image.setText(_translate("MainWindow", "Abrir Imagem"))
        self.save_image.setText(_translate("MainWindow", "Salvar"))
        self.close.setText(_translate("MainWindow", "Fechar"))
        self.action_bin.setText(_translate("MainWindow", "Threshold Binário"))
        self.action_bin_inv.setText(_translate("MainWindow", "Threshold Binário Invertido"))
        self.action_trunc.setText(_translate("MainWindow", "Threshold Truncado"))
        self.action_zero.setText(_translate("MainWindow", "Threshold Zero"))
        self.action_zero_inv.setText(_translate("MainWindow", "Threshold Zero Invertido"))
        self.action_adap_gau.setText(_translate("MainWindow", "Threshold Adaptativo Gaussiano"))
        self.action_adap_med.setText(_translate("MainWindow", "Threshold Adaptativo Médio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
