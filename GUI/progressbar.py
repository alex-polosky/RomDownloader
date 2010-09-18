# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressbar.ui'
#
# Created: Fri Jun 04 12:59:51 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ProgressBar(QtGui.QWidget):
    def setupUi(self, ProgressBar):
        ProgressBar.setObjectName("ProgressBar")
        ProgressBar.resize(261, 101)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressBar.sizePolicy().hasHeightForWidth())
        ProgressBar.setSizePolicy(sizePolicy)
        ProgressBar.setMaximumSize(QtCore.QSize(262, 101))
        self.progressBar = QtGui.QProgressBar(ProgressBar)
        self.progressBar.setGeometry(QtCore.QRect(10, 50, 241, 21))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.Downloading = QtGui.QLabel(ProgressBar)
        self.Downloading.setGeometry(QtCore.QRect(0, 0, 261, 41))
        self.Downloading.setObjectName("Downloading")
        self.partofpart = QtGui.QLabel(ProgressBar)
        self.partofpart.setGeometry(QtCore.QRect(0, 80, 261, 20))
        self.partofpart.setObjectName("partofpart")

        #self.retranslateUi(ProgressBar)
        #QtCore.QMetaObject.connectSlotsByName(ProgressBar)

    def retranslateUi(self, ProgressBar, part1, part2):
        ProgressBar.setWindowTitle(QtGui.QApplication.translate("ProgressBar", "Downloading", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("ProgressBar", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.Downloading.setText(QtGui.QApplication.translate("ProgressBar", "<font size=\'25\'><center>Downloading...</center></font>", None, QtGui.QApplication.UnicodeUTF8))
        self.partofpart.setText(QtGui.QApplication.translate("ProgressBar", "<center>Part %s of %s</center>" %(part1, part2), None, QtGui.QApplication.UnicodeUTF8))

    def __init__(self, part1="", part2="", parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi(self, part1, part2)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    PB = Ui_ProgressBar(2, (3))
    PB.show()
    sys.exit(app.exec_())

