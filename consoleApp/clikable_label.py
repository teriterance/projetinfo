from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from domino import Domino
from PyQt5.QtCore import *

class MyQLabel(QLabel):
    '''fodop'''
    def __init__(self, parent, dom):
        self.dom = dom
        super().__init__(parent)
    clicked = pyqtSignal(Domino)
    rightClicked = pyqtSignal()

    def mousePressEvent(self,ev):
        if ev.button() == Qt.RightButton:
            self.rightClicked.emit()
        else:
            self.clicked.emit(self.dom)