from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel,
    QHBoxLayout
)
from PyQt5.QtCore import Qt, pyqtSignal

class TopBar(QWidget):
    back_requested = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("topbar")
        self.setFixedHeight(50)

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(20)

        self.back_btn = QPushButton("Back")
        layout.addWidget(self.back_btn, alignment=Qt.AlignLeft)

        self.back_btn.clicked.connect(self.back_requested.emit)

        self.title_label = QLabel("Main")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label, stretch=1)

        layout.addStretch()
        self.setLayout(layout)