# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageEditor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1008, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QtCore.QSize(1, 1))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(11, 11, 993, 737))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelImage = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelImage.sizePolicy().hasHeightForWidth())
        self.labelImage.setSizePolicy(sizePolicy)
        self.labelImage.setMouseTracking(False)
        self.labelImage.setAutoFillBackground(False)
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("../imgs/handExample.jpg"))
        self.labelImage.setScaledContents(False)
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setWordWrap(False)
        self.labelImage.setObjectName("labelImage")
        self.verticalLayout_2.addWidget(self.labelImage)
        self.listWidgetActionQueue = QtWidgets.QListWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetActionQueue.sizePolicy().hasHeightForWidth())
        self.listWidgetActionQueue.setSizePolicy(sizePolicy)
        self.listWidgetActionQueue.setMaximumSize(QtCore.QSize(16777215, 50))
        self.listWidgetActionQueue.setSizeIncrement(QtCore.QSize(1, 1))
        self.listWidgetActionQueue.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidgetActionQueue.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidgetActionQueue.setObjectName("listWidgetActionQueue")
        self.verticalLayout_2.addWidget(self.listWidgetActionQueue)
        self.scrollAreaDescription = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaDescription.setEnabled(True)
        self.scrollAreaDescription.setGeometry(QtCore.QRect(220, 760, 330, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaDescription.sizePolicy().hasHeightForWidth())
        self.scrollAreaDescription.setSizePolicy(sizePolicy)
        self.scrollAreaDescription.setAccessibleName("")
        self.scrollAreaDescription.setAutoFillBackground(True)
        self.scrollAreaDescription.setFrameShape(QtWidgets.QFrame.HLine)
        self.scrollAreaDescription.setWidgetResizable(True)
        self.scrollAreaDescription.setObjectName("scrollAreaDescription")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 326, 527))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 300, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPopUpTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPopUpTitle.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelPopUpTitle.setObjectName("labelPopUpTitle")
        self.verticalLayout.addWidget(self.labelPopUpTitle)
        self.labelPopUpDescriptionText = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPopUpDescriptionText.sizePolicy().hasHeightForWidth())
        self.labelPopUpDescriptionText.setSizePolicy(sizePolicy)
        self.labelPopUpDescriptionText.setMinimumSize(QtCore.QSize(298, 0))
        self.labelPopUpDescriptionText.setMaximumSize(QtCore.QSize(298, 16777215))
        self.labelPopUpDescriptionText.setText("")
        self.labelPopUpDescriptionText.setWordWrap(True)
        self.labelPopUpDescriptionText.setObjectName("labelPopUpDescriptionText")
        self.verticalLayout.addWidget(self.labelPopUpDescriptionText)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.labelPopUpImageDefaultText = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPopUpImageDefaultText.setObjectName("labelPopUpImageDefaultText")
        self.verticalLayout.addWidget(self.labelPopUpImageDefaultText)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.labelPopUpImageModifiedImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPopUpImageModifiedImage.sizePolicy().hasHeightForWidth())
        self.labelPopUpImageModifiedImage.setSizePolicy(sizePolicy)
        self.labelPopUpImageModifiedImage.setMinimumSize(QtCore.QSize(289, 150))
        self.labelPopUpImageModifiedImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelPopUpImageModifiedImage.setText("")
        self.labelPopUpImageModifiedImage.setPixmap(QtGui.QPixmap("../imgs/wolf2.png"))
        self.labelPopUpImageModifiedImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPopUpImageModifiedImage.setObjectName("labelPopUpImageModifiedImage")
        self.verticalLayout.addWidget(self.labelPopUpImageModifiedImage)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.labelPopUpModifiedImageText = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPopUpModifiedImageText.sizePolicy().hasHeightForWidth())
        self.labelPopUpModifiedImageText.setSizePolicy(sizePolicy)
        self.labelPopUpModifiedImageText.setObjectName("labelPopUpModifiedImageText")
        self.verticalLayout.addWidget(self.labelPopUpModifiedImageText)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.labelPopUpImageDefaultImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPopUpImageDefaultImage.sizePolicy().hasHeightForWidth())
        self.labelPopUpImageDefaultImage.setSizePolicy(sizePolicy)
        self.labelPopUpImageDefaultImage.setMinimumSize(QtCore.QSize(289, 150))
        self.labelPopUpImageDefaultImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelPopUpImageDefaultImage.setText("")
        self.labelPopUpImageDefaultImage.setPixmap(QtGui.QPixmap("../imgs/wolf1.png"))
        self.labelPopUpImageDefaultImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPopUpImageDefaultImage.setObjectName("labelPopUpImageDefaultImage")
        self.verticalLayout.addWidget(self.labelPopUpImageDefaultImage)
        self.scrollAreaDescription.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
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
        self.actionThresholds = QtWidgets.QAction(MainWindow)
        self.actionThresholds.setObjectName("actionThresholds")
        self.actiona = QtWidgets.QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.actionFeatureTracking = QtWidgets.QAction(MainWindow)
        self.actionFeatureTracking.setEnabled(True)
        self.actionFeatureTracking.setObjectName("actionFeatureTracking")
        self.actionOperacoes = QtWidgets.QAction(MainWindow)
        self.actionOperacoes.setEnabled(True)
        self.actionOperacoes.setObjectName("actionOperacoes")
        self.menuFile.addAction(self.actionOpenImage)
        self.menuFile.addAction(self.actionSaveImage)
        self.menuFile.addAction(self.actionClose)
        self.menuFilters.addAction(self.actionThresholds)
        self.menuFilters.addSeparator()
        self.menuFilters.addAction(self.actionFeatureTracking)
        self.menuFilters.addSeparator()
        self.menuFilters.addAction(self.actionOperacoes)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())

        self.retranslateUi(MainWindow)
        self.listWidgetActionQueue.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.listWidgetActionQueue.setSortingEnabled(True)
        self.labelPopUpTitle.setText(_translate("MainWindow", "Title"))
        self.labelPopUpImageDefaultText.setText(_translate("MainWindow", "Imagem Original:"))
        self.labelPopUpModifiedImageText.setText(_translate("MainWindow", "Imagem com Efeito aplicado:"))
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
        self.actionThresholds.setText(_translate("MainWindow", "Thresholds"))
        self.actiona.setText(_translate("MainWindow", "a"))
        self.actionFeatureTracking.setText(_translate("MainWindow", "Feature Tracking"))
        self.actionOperacoes.setText(_translate("MainWindow", "Operações"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
