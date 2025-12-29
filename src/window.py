from PyQt5.QtWidgets import (
    QWidget
)
import sys
class MainWindow(QWidget):
    def __init__(self, title, width, height):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(width, height)