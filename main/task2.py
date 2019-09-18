# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        MainWindow.setStyleSheet("background-image: url(:/Imgs/wallBlue);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 10, 791, 541))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelImage = QtWidgets.QLabel(self.verticalWidget)
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.verticalLayout_2.addWidget(self.labelImage)
        self.listWidgetActionQueue = QtWidgets.QListWidget(self.verticalWidget)
        self.listWidgetActionQueue.setMaximumSize(QtCore.QSize(16777215, 50))
        self.listWidgetActionQueue.setObjectName("listWidgetActionQueue")
        self.verticalLayout_2.addWidget(self.listWidgetActionQueue)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFilters = QtWidgets.QMenu(self.menubar)
        self.menuFilters.setObjectName("menuFilters")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenImage = QtWidgets.QAction(MainWindow)
        self.actionOpenImage.setObjectName("actionOpenImage")
        self.actionSaveImage = QtWidgets.QAction(MainWindow)
        self.actionSaveImage.setObjectName("actionSaveImage")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionThresholdBinary = QtWidgets.QAction(MainWindow)
        self.actionThresholdBinary.setObjectName("actionThresholdBinary")
        self.actionThresholdBinaryInverse = QtWidgets.QAction(MainWindow)
        self.actionThresholdBinaryInverse.setObjectName("actionThresholdBinaryInverse")
        self.actionThresholdTruncate = QtWidgets.QAction(MainWindow)
        self.actionThresholdTruncate.setObjectName("actionThresholdTruncate")
        self.actionThresholdZero = QtWidgets.QAction(MainWindow)
        self.actionThresholdZero.setObjectName("actionThresholdZero")
        self.actionThresholdZeroInverse = QtWidgets.QAction(MainWindow)
        self.actionThresholdZeroInverse.setObjectName("actionThresholdZeroInverse")
        self.actionThresholdAdaptativeGaussian = QtWidgets.QAction(MainWindow)
        self.actionThresholdAdaptativeGaussian.setObjectName("actionThresholdAdaptativeGaussian")
        self.actionThresholdAdaptativeMean = QtWidgets.QAction(MainWindow)
        self.actionThresholdAdaptativeMean.setObjectName("actionThresholdAdaptativeMean")
        self.actiona = QtWidgets.QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.menuFile.addAction(self.actionOpenImage)
        self.menuFile.addAction(self.actionSaveImage)
        self.menuFile.addAction(self.actionClose)
        self.menuFilters.addAction(self.actionThresholdBinary)
        self.menuFilters.addAction(self.actionThresholdBinaryInverse)
        self.menuFilters.addAction(self.actionThresholdTruncate)
        self.menuFilters.addAction(self.actionThresholdZero)
        self.menuFilters.addAction(self.actionThresholdZeroInverse)
        self.menuFilters.addAction(self.actionThresholdAdaptativeGaussian)
        self.menuFilters.addAction(self.actionThresholdAdaptativeMean)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())

        self.retranslateUi(MainWindow)
        self.listWidgetActionQueue.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.listWidgetActionQueue.setSortingEnabled(True)
        self.menuFile.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuFilters.setTitle(_translate("MainWindow", "Filtros"))
        self.actionOpenImage.setText(_translate("MainWindow", "Abrir Imagem"))
        self.actionSaveImage.setText(_translate("MainWindow", "Salvar"))
        self.actionClose.setText(_translate("MainWindow", "Fechar"))
        self.actionThresholdBinary.setText(_translate("MainWindow", "Threshold Binário"))
        self.actionThresholdBinaryInverse.setText(_translate("MainWindow", "Threshold Binário Invertido"))
        self.actionThresholdTruncate.setText(_translate("MainWindow", "Threshold Truncado"))
        self.actionThresholdZero.setText(_translate("MainWindow", "Threshold Zero"))
        self.actionThresholdZeroInverse.setText(_translate("MainWindow", "Threshold Zero Invertido"))
        self.actionThresholdAdaptativeGaussian.setText(_translate("MainWindow", "Threshold Adaptativo Gaussiano"))
        self.actionThresholdAdaptativeMean.setText(_translate("MainWindow", "Threshold Adaptativo Médio"))
        self.actiona.setText(_translate("MainWindow", "a"))
import mainResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
