from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore
import os
from os.path import abspath, dirname


class FileDialog:

    def __init__(self):
        self.states = []

    def openFile(self, directory='', forOpen=True, fmt='', isFolder=False):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.DontUseCustomDirectoryIcons
        dialog = QFileDialog()
        dialog.setOptions(options)

        if directory == '':
            directory = self.getCurrentPath()
            print(directory)

        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)

        # ARE WE TALKING ABOUT FILES OR FOLDERS
        if isFolder:
            dialog.setFileMode(QFileDialog.DirectoryOnly)
        else:
            dialog.setFileMode(QFileDialog.AnyFile)
        # OPENING OR SAVING
        dialog.setAcceptMode(QFileDialog.AcceptOpen) if forOpen else dialog.setAcceptMode(QFileDialog.AcceptSave)

        # SET FORMAT, IF SPECIFIED
        if fmt != '' and isFolder is False:
            dialog.setDefaultSuffix(fmt)
            dialog.setNameFilters([f'{fmt} (*.{fmt})'])

        # SET THE STARTING DIRECTORY
        if directory != '':
            dialog.setDirectory(str(directory + "/resources/imgs/"))
        else:
            dialog.setDirectory(str(""))

        if dialog.exec_() == QDialog.Accepted:
            path = dialog.selectedFiles()[0]  # returns a list
            return path
        else:
            return ''

    def saveFile(self, directory='', forOpen=False,):
        filename = QFileDialog.getSaveFileName(self, "Save file", '', '.jpg')
        return filename

    def getCurrentPath(self):
        dirpath = os.getcwd()
        return dirpath