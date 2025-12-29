from PyQt5.QtWidgets import (
    QPushButton
)
from PyQT5.QtCore import pyqtSignal, QIcon

class PageButton(QPushButton):
    page = pyqtSignal(str)
    def __init__(self, title, width, height, x, y):
        super().__init__(pageName)
        self.button.setFixedSize(width, height)
        