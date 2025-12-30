from PyQt5.QtWidgets import ( 
    QWidget, QVBoxLayout, QLabel,
    QPushButton
)
from src.pages.stats import (
     CorrCovar, DescStats, InferStats,
     NonParametric
)

class StatsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
    
        self.page_name="Statistics"

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.descstats      = DescStats() #index 1
        self.corrcovar      = CorrCovar() #index 2
        self.inferstats     = InferStats() #index3
        self.nonparametric  = NonParametric() #index 4

        # buttons
        descstatsbtn        = QPushButton("Descriptive Statistics")
        corrcovarbtn        = QPushButton("Correlation && Covariance")
        inferstatsbtn       = QPushButton("Inferential Statistics")
        nonparametricbtn    = QPushButton("Non-Parametric && Multi-Group Analysis")

        descstatsbtn.setFixedSize(300, 30)
        corrcovarbtn.setFixedSize(300, 30)
        inferstatsbtn.setFixedSize(300, 30)
        nonparametricbtn.setFixedSize(300, 30)

        # .addWidget
        layout.addWidget(descstatsbtn)
        layout.addWidget(corrcovarbtn)
        layout.addWidget(inferstatsbtn)
        layout.addWidget(nonparametricbtn)
        layout.addStretch(10)

        # .clicked.connect

        descstatsbtn.clicked.connect(lambda: self.parent.go_to(self.parent.descstats))
        corrcovarbtn.clicked.connect(lambda: self.parent.go_to(self.parent.corrcovar))
        inferstatsbtn.clicked.connect(lambda: self.parent.go_to(self.parent.inferstats))
        nonparametricbtn.clicked.connect(lambda: self.parent.go_to(self.parent.nonparametric))