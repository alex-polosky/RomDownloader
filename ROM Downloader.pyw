from PyQt4 import QtGui

from engine import DownloadLink
from searcher import Crawler
from GUI import *

import sys  
app = QtGui.QApplication(sys.argv)
MainWindow = GUIFill()
sys.exit(app.exec_())
