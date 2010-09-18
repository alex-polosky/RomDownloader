# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

from threading import Thread

from engine import DownloadLink
from searcher import Crawler
from progressbar import Ui_ProgressBar

class ProgBar(QThread):

    def run(self):
        import time
        time.sleep(5)
        del time
        self.emit(SIGNAL("dl(PyQt_PyObject)"))
        
##    def run(self):
##        if Ui_MainWindow.dl:
##            self.PB.show()
##            while Ui_MainWindow.dl:
##                pass
##            self.PB.hide()
##
##    def __init__(self, part1, part2):
##        self.PB = Ui_ProgressBar(part1, part2)

class Ui_MainWindow(QtGui.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 388)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(511, 388))
        MainWindow.setMaximumSize(QtCore.QSize(511, 388))
        MainWindow.setMouseTracking(False)
        
        self.comboBox = QtGui.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.comboBox.setObjectName("comboBox")
        
        self.lineEdit = QtGui.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 411, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton = QtGui.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(430, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtGui.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtGui.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 360, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtGui.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 360, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.lineEdit_2 = QtGui.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 360, 321, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.treeWidget = QtGui.QTreeWidget(MainWindow)
        self.treeWidget.setGeometry(QtCore.QRect(10, 70, 481, 281))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setFrameShape(QtGui.QFrame.WinPanel)
        self.treeWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setTabKeyNavigation(False)
        self.treeWidget.setObjectName("treeWidget")

        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setRootIsDecorated(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setTabOrder(self.comboBox, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.treeWidget)
        MainWindow.setTabOrder(self.treeWidget, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.lineEdit_2)

        self.fillcomboBox()
        self.colortextbox()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ROM Downloader", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setProperty("color", QtGui.QApplication.translate("MainWindow", "QtGui.QColor(0, 0, 0) ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "Game", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Catalog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "ROM Name", None, QtGui.QApplication.UnicodeUTF8))

class GUIFill(Ui_MainWindow):

    def fillcomboBox(self):
        self.objs = {0:"All Systems"}
        objs = [x for x in DownloadLink.abbrs2]
        objs.sort()
        counter = 0
        self.comboBox.addItem("")
        self.comboBox.setItemText(counter, QtGui.QApplication.translate("MainWindow", "All Systems", None, QtGui.QApplication.UnicodeUTF8))
        counter += 1
        for x in objs:
            self.comboBox.addItem("")
            if x == 'Sony PSP':
                self.comboBox.setItemText(counter, QtGui.QApplication.translate("MainWindow", "Sony PSP [NOT WORKING]", None, QtGui.QApplication.UnicodeUTF8))
            else:
                self.comboBox.setItemText(counter, QtGui.QApplication.translate("MainWindow", x, None, QtGui.QApplication.UnicodeUTF8))
            self.objs[counter] = x
            counter += 1

    def colortextbox(self):
        palette = self.lineEdit_2.palette()
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Text, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Base, QtGui.QColor(224, 223, 227))
        self.lineEdit_2.setPalette(palette)
        self.path = os.getcwd()
        self.lineEdit_2.setText(QtGui.QApplication.translate("MainWindow", self.path, None, QtGui.QApplication.UnicodeUTF8))

    def search(self):
        self.treeWidget.clear()
        try:
            del self.item
        except:
            pass
        try:
            del self.C
        except:
            pass
        try:
            del self.games
        except:
            pass
        qApp.setOverrideCursor(Qt.WaitCursor)
        self.system = str(self.objs[self.comboBox.currentIndex()])
        if self.system == 'All Systems':
            qApp.restoreOverrideCursor()
            QMessageBox.information(self, self.tr("ROM Downloader"),
                                    self.tr("Search is not supported for All Systems"))
            del self.system
            return None
        self.game = str(self.lineEdit.text())
        self.C = Crawler(self.game, self.system)
        qApp.restoreOverrideCursor()
        self.games = {}
        for x in self.C.games:
            self.games[x[1]] = x[0]
        if len(self.C.games) == 0:
            QMessageBox.information(self, self.tr("ROM Downloader"),
                                    self.tr("No roms found."))
        else:
            games = []
            for x in self.games:
                games.append(x)
            games.sort()
            for game in games:
                item = QTreeWidgetItem()
                item.setText(0, game)
                self.treeWidget.addTopLevelItem(item)
        return None

    def download(self):
        try:
            print(self.system)
        except:
            QMessageBox.information(self, self.tr("ROM Downloader"),
                                    self.tr("No search selected"))
            return None
        print(self.item)
        formattedtext ='''\
<html>
<center>
You are downloading<br />%s<br />for the<br />%s
</center>
</html>
''' %(self.item, self.system)        
        reply = QtGui.QMessageBox.question(self, 'Downloading',
                                   formattedtext,
                                   QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.curgame = self.games[str(self.item)]
            self.dlfile()
            
        else:
            print("No")
        return None

##    def dlfile(self):
##        QtGui.QMessageBox.question(self, "Downloading",
##                                       "<html><center>There are %s parts<br />Please wait while all are downloaded</center></html>" %(len(self.curgame)),
##                                       QtGui.QMessageBox.NoButton)
##        counter = 1
##        for x in self.curgame:
##            print(self)
##            # Set the bar
##            global dl, PB
##            dl = 1
##            PB = Ui_ProgressBar(counter, len(self.curgame))
##            PB.show()
##            # Download it
##            #DL = DownloadLink(x, DownloadLink.abbrs2[str(self.system)])
##            import time
##            time.sleep(5)
##            del time
##            PB.hide()
##            self.dl = 0
##            counter += 1

    def dlfile(self):
        QtGui.QMessageBox.question(self, "Downloading",
                                       "<html><center>There are %s parts<br />Please wait while all are downloaded</center></html>" %(len(self.curgame)),
                                       QtGui.QMessageBox.NoButton)
        counter = 1
        for x in self.curgame:
            print(self)
            # Set the bar
            self.PB = Ui_ProgressBar(counter, len(self.curgame))
            self.PB.show()

            # START THREADING
            self.dlThread = ProgBar()
            self.dlThread.start()
            
            # Download it
            #DL = DownloadLink(x, DownloadLink.abbrs2[str(self.system)])
            #import time
            #time.sleep(5)
            #del time

            # KEEP CHECKING FOR DL CHANGE
            self.connect(dlThread,
                       QtCore.SIGNAL("dl()"),
                       self.killPB)
            
            counter += 1

    def killPB(self):
        self.dlThread.join()
        self.PB.hide()

##    def dlPBrun(self):
##        import time
##        time.sleep(5)
##        del time
##        self.emit(SIGNAL("dl(PyQt_PyObject)"))
            
    def onTreeWidgetItem(self, item, column):
        try:
            self.item = item.text(0)
        except:
            try:
                del self.item
            except:
                pass

    def catalog(self):
       QMessageBox.information(self, self.tr("ROM Downloader"),
                                    self.tr("This feature is not yet implemented"))

    def browse(self):
        QMessageBox.information(self, self.tr("ROM Downloader"),
                                    self.tr("This feature is not yet implemented"))
        #filename=QFileDialog.getOpenFileName("", "*.py", self, "FileDialog")

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.pushButton_2, SIGNAL("clicked()"),
                     self.search)
        self.connect(self.pushButton_3, SIGNAL("clicked()"),
                     self.download)
        self.connect(self.pushButton, SIGNAL("clicked()"),
                     self.catalog)
        self.connect(self.pushButton_4, SIGNAL("clicked()"),
                     self.browse)
        self.treeWidget.currentItemChanged.connect(self.onTreeWidgetItem)
        self.show()



