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
from src.fileDialog import FileDialog
from src.dialogOptions import Ui_Dialog

from src.imageEditor import Ui_MainWindow
import src.imageEditor as ie


class MainWindow(QMainWindow, Ui_MainWindow, FileDialog, Ui_Dialog):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        #self.menuFilters.installEventFilter(self)
        self.states = []
        self.appliedFilters = []
        self.temp = ''
        self.cvImg = ''
        self.cvImg2 = ''
        self.addMenuTriggers()
        self.filename = ''
        self.maxThres = 255
        self.thres = 127
        self.thresType = ''

        self.item = 'other'

    def openFileSettings(self):
        filename = FileDialog.openFile(self, '', True, "", False)

        if filename is None or filename is '':
            return

        self.filename = filename

        pixmap = QPixmap(self.filename)

        pixmap = pixmap.scaled(self.labelImage.size(), Qt.KeepAspectRatio)
        self.labelImage.setPixmap(pixmap)

        self.cvImg = cv2.imread(self.filename, 0)
        self.cvImg2 = cv2.imread(self.filename)

    def saveFileSettings(self):
        filepath = FileDialog.saveFile(self, '', True)

        if filepath[0] is '':
            return

        self.labelImage.pixmap().toImage().save(filepath[0] + '.jpg')

    def acceptDialog(self):
        self.Dialog.close()

    def closeDialog(self):
        self.Dialog.close()

    def openOptionsDialog(self, type):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        thresholds = ['Limiarização Binária', 'Limiarização Binária Invertida', 'Limiarização Truncada',
                          'Limiarização Zero', 'Limiarização Zero Invertida', 'Limiarização Adaptativa Média',
                          'Limiarização Adaptativa Gaussiana']
            # self.listViewOptions.addItems(thresholds)
        self.ui.listWidgetOptions.addItems(thresholds)

        self.ui.listWidgetOptions.itemClicked.connect(partial(self.dialogOptionClicked, type))

        self.ui.buttonBox.accepted.connect(self.acceptDialog)
        self.ui.buttonBox.rejected.connect(self.closeDialog)

        self.scrollAreaDescription.setVisible(False)

        self.ui.scrollAreaDescription.setVisible(False)

        if self.ui.textEditInputValue1 is not None:
            self.ui.textEditInputValue1.textChanged.connect(self.getInputFromDialog)
            self.ui.textEditInputValue1.setText('255')
            self.ui.labelInputValue1.setText('Max Binary Value')
            self.ui.textEditInputValue1.setToolTip('The value used with the Binary thresholding operations (to set the chosen pixels)')

        if self.ui.textEditInputValue2 is not None:
            self.ui.textEditInputValue2.textChanged.connect(self.getInputFromDialog)
            self.ui.textEditInputValue2.setText('127')
            self.ui.labelInputValue2.setText('Threshold Value')
            self.ui.textEditInputValue2.setToolTip('The thresh value with respect to which the thresholding operation is made')

        self.Dialog.show()
        self.Dialog.exec_()

    def dialogOptionClicked(self, type, item):
        if type == 'threshold':
            self.ui.scrollAreaDescription.setVisible(True)
            text = item.text()

            self.buildThresholdDialogOptions(text)
            self.ui.labelDescriptionTitle.setText(text)

            self.threshold(text)

            if self.filename is None or self.filename is '':
                return

            self.displayImagesOnDialog()

    def displayImagesOnDialog(self):
        pixmap = QPixmap(self.filename)
        print(self.ui.labelOriginalImage.size())
        pixmap = pixmap.scaled(self.ui.labelOriginalImage.size(), Qt.KeepAspectRatio)
        self.ui.labelOriginalImage.setPixmap(pixmap)
        self.displayImageGray(self.ui.labelModifiedImage)

    def itemClicked(self, item):
        print(item.text())
        index = self.listWidgetActionQueue.row(item)
        self.labelImage = self.states[index]

    def threshold(self, type):

        self.thresType = type

        if isinstance(self.cvImg, str):
            return

        if self.maxThres is not None:
            max = self.maxThres
        else:
            max = 255
        if self.thres is not None:
            thres = self.thres
        else:
            thres = 127

        if type == 'Limiarização Binária':
            ret, thresh1 = cv2.threshold(self.cvImg, thres, max, cv2.THRESH_BINARY)
            self.temp = thresh1

            self.ui.labelDescription.setText('A limiarização será binária, ou seja, terá somente dois valores '
                                             'possíveis para cada pixel.')

            # self.listWidgetActionQueue.addItem('Threshold Binário')
        elif type == 'Limiarização Binária Invertida':
            ret, thresh2 = cv2.threshold(self.cvImg, thres, max, cv2.THRESH_BINARY_INV)
            self.temp = thresh2

            self.ui.labelDescription.setText('A limiarização será binária, ou seja, terá somente dois valores '
                                             'possíveis para cada pixel. Porém serão o inverso da operação binária '
                                             'original.')
            # self.listWidgetActionQueue.addItem('Threshold Binário Invertido')
        elif type == 'Limiarização Truncada':
            ret, thresh3 = cv2.threshold(self.cvImg, thres, max, cv2.THRESH_TRUNC)
            self.temp = thresh3
            # self.listWidgetActionQueue.addItem('Threshold Truncado')
        elif type == 'Limiarização Zero':
            ret, thresh4 = cv2.threshold(self.cvImg, thres, max, cv2.THRESH_TOZERO)
            self.temp = thresh4
            # self.listWidgetActionQueue.addItem('Threshold Zero')
        elif type == 'Limiarização Zero Invertida':
            ret, thresh5 = cv2.threshold(self.cvImg, thres, max, cv2.THRESH_TOZERO_INV)
            self.temp = thresh5
            # self.listWidgetActionQueue.addItem('Threshold Zero Invertido')
        elif type == 'Limiarização Adaptativa Média':
            img = cv2.medianBlur(self.cvImg, 5)
            ret, th1 = cv2.threshold(img, thres, 255, cv2.THRESH_BINARY)
            th2 = cv2.adaptiveThreshold(th1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                        cv2.THRESH_BINARY, 11, 2)
            self.temp = th2
            # self.listWidgetActionQueue.addItem('Threshold Adaptativo Médio')
        elif type == 'Limiarização Adaptativa Gaussiana':
            img = cv2.medianBlur(self.cvImg, 5)
            ret, th1 = cv2.threshold(img, thres, 255, cv2.THRESH_BINARY)
            th3 = cv2.adaptiveThreshold(th1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                        cv2.THRESH_BINARY, 11, 2)
            self.temp = th3
            # self.listWidgetActionQueue.addItem('Threshold Adaptativo Gaussiano')

            print(self.temp)

    def displayImageGray(self, labelImage):
        if len(self.temp.shape) < 3 or self.temp.shape[2] == 1:
            image = cv2.cvtColor(self.temp, cv2.COLOR_GRAY2RGB)
        else:
            image = cv2.cvtColor(self.temp, cv2.COLOR_BGR2RGB)

        height, width, byteValue = image.shape
        byteValue = byteValue * width

        qimage = QImage(image, width, height, byteValue, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(labelImage.size(), Qt.KeepAspectRatio)

        labelImage.setPixmap(pixmap)
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

            # img.scaled(self.labelImage.size(),Qt.KeepAspectRatio)
            # img = img.rgbSwapped()
            self.labelImage.setPixmap(QPixmap.fromImage(img))
            self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
            print("displayed")
            self.states.append(self.labelImage)
        else:
            print(self.temp.shape)

    def getInputFromDialog(self):

        if self.ui.textEditInputValue2 is not None:
            mytext = self.ui.textEditInputValue2.toPlainText()
            if mytext is '':
                mytext = "127"

            self.thres = int(mytext, 10)
        else:
            self.thres = 127

        if self.ui.textEditInputValue1 is not None:
            mytext = self.ui.textEditInputValue1.toPlainText()
            if mytext is '':
                mytext = "255"
            self.maxThres = int(mytext, 10)
        else:
            self.maxThres = 255

        if self.temp != '':
            self.threshold(self.thresType)
            self.displayImagesOnDialog()

    def configurePopUp(self):
        if self.scrollAreaDescription.isVisible():
            self.labelPopUpTitle.setText("Limiarização")
            self.labelPopUpDescriptionText.setText("Limiarização é um processo de segmentação de imagens que se baseia na "
                                               "diferença dos níveis de cinza que compõe diferentes objetos de uma "
                                               "imagem. A partir de um limiar estabelecido de acordo com as "
                                               "características dos objetos que se quer isolar, a imagem pode ser "
                                               "segmentada em dois grupos: o grupo de pixels com níveis de cinza "
                                               "abaixo do limiar e o grupo de pixels com níveis de cinza acima do "
                                               "limiar. Em uma imagem limiarizada, atribui-se um valor fixo para "
                                               "todos os pixels de mesmo grupo.")
            self.labelPopUpDescriptionText.adjustSize()
            self.labelPopUpModifiedImageText.setText("Imagem com limiarização aplicada.")
            #self.labelPopUpImageDefaultImage.


            pixmap = QPixmap('C:/Users/Caio/PycharmProjects/image_editor/resources/imgs/wolf1.png')
            pixmap = pixmap.scaled(self.labelPopUpImageDefaultImage.size(), Qt.KeepAspectRatio)
            self.labelPopUpImageDefaultImage.setPixmap(pixmap)

            pixmap = QPixmap('C:/Users/Caio/PycharmProjects/image_editor/resources/imgs/wolf2.png')
            pixmap = pixmap.scaled(self.labelPopUpImageModifiedImage.size(), Qt.KeepAspectRatio)
            self.labelPopUpImageModifiedImage.setPixmap(pixmap)

    #UI Builders

    def addMenuTriggers(self):
        self.menuFilters.setToolTipsVisible(True)
        self.actionOpenImage.triggered.connect(self.openFileSettings)
        self.actionSaveImage.triggered.connect(self.saveFileSettings)
        self.actionThresholds.triggered.connect(partial(self.openOptionsDialog, 'threshold'))
        # self.actionFeatureTracking.triggered.connect(self.featureTracking)
        self.actionFeatureTracking.setVisible(False)
        #self.actionOperacoes.setVisible(False)
        self.actionOperacoes.triggered.connect(partial(self.openOptionsDialog, 'operations'))
        self.listWidgetActionQueue.itemClicked.connect(self.itemClicked)
        # self.actionThresholds.installEventFilter(self)
        # self.scrollAreaDescription.setVisible(False)

    def buildThresholdDialogOptions(self, type):

        if type == 'Limiarização Binária':
            self.ui.labelDescription.setText('A limiarização será binária, ou seja, terá somente dois valores '
                                             'possíveis para cada pixel.')

        elif type == 'Limiarização Binária Invertida':
            self.ui.labelDescription.setText('A limiarização será binária, ou seja, terá somente dois valores '
                                             'possíveis para cada pixel. Porém serão o inverso da operação binária '
                                             'original.')
        elif type == 'Limiarização Truncada':
            self.ui.labelDescription.setText('')
        elif type == 'Limiarização Zero':
            self.ui.labelDescription.setText('')
        elif type == 'Limiarização Zero Invertida':
            self.ui.labelDescription.setText('')
        elif type == 'Limiarização Adaptativa Média':
            self.ui.labelDescription.setText('')
        elif type == 'Limiarização Adaptativa Gaussiana':
            self.ui.labelDescription.setText('')

    def buildOperationsDialogOptions(self, type):

        if type == 'blur':
            self.ui.labelDescription.setText('A limiarização será binária, ou seja, terá somente dois valores '
                                             'possíveis para cada pixel.')

        elif type == 'Limiarização Binária Invertida':
            self.ui.labelDescription.setText('A limiarização será binária, ou seja, terá somente dois valores '
                                             'possíveis para cada pixel. Porém serão o inverso da operação binária '
                                             'original.')
        elif type == 'Limiarização Truncada':
            self.ui.labelDescription.setText('')
        elif type == 'Limiarização Zero':
            self.ui.labelDescription.setText('')
        elif type == 'Limiarização Zero Invertida':
            self.ui.labelDescription.setText('')
        elif type == 'Limiarização Adaptativa Média':
            self.ui.labelDescription.setText('')
        elif type == 'Limiarização Adaptativa Gaussiana':
            self.ui.labelDescription.setText('')

    #Events
    def resizeEvent(self, event):

        if self.cvImg is '':
            pass

        size = self.labelImage.size()
        print(size)
        print(self.size())
        pixmap = QPixmap(self.filename)
        pixmap = pixmap.scaled(size, Qt.KeepAspectRatio)
        self.labelImage.setPixmap(pixmap)
        self.labelImage.adjustSize()

    def eventFilter(self, obj, event):
        # action = self.sender()
        # print(obj.text())
        print(event)
        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton:
                pos = event.pos()
                action = self.menuFilters.actionAt(pos)

                if action is not None:
                    if action is self.actionThresholds:
                        width = self.menuFilters.width() - self.menuFile.width() + self.menuFilters.width()
                        pass
                        #self.scrollAreaDescription.setVisible(True)
                        #self.scrollAreaDescription.setAutoFillBackground(True)
                        #self.scrollAreaDescription.move(width * 1.25, 0)
                        #self.configurePopUp()
                    else:
                        pass
                        #self.scrollAreaDescription.setVisible(False)
                else:
                    pass
                    # self.scrollAreaDescription.setVisible(False)

            else:
                pass  # do other stuff

        return QMainWindow.eventFilter(self, obj, event)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
