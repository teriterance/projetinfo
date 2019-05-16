from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyQLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
    clicked = pyqtSignal()
    rightClicked = pyqtSignal()

    def mousePressEvent(self,ev):
        if ev.button() == Qt.RightButton:
            self.rightClicked.emit()
        else:
            self.clicked.emit()