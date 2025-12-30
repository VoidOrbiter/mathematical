from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, 
    QPushButton, QStackedWidget, QVBoxLayout
)
import sys
from src.pages.stats import (
    CorrCovar, DescStats, InferStats, StatsPage,
    NonParametric
)
from src.modules.menus.topbar import TopBar

class MainWindow(QWidget):
    def __init__(self, title, width, height):
        super().__init__()

        self.history = []

        # layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Topbar
        self.topbar = TopBar()
        main_layout.addWidget(self.topbar)  # always visible at top

        # Stacked widget
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)  # pages go below topbar

        # Main Page
        self.main_page = QWidget()
        self.main_page.page_name = "Mathematical!"

        #button container
        button_container = QWidget()
        button_layout = QGridLayout(button_container)
        button_container.setLayout(button_layout)

        # Pages
        self.statspage = StatsPage(self)
        self.calcpage = QWidget()
        self.stack.addWidget(self.main_page)   # index 0
        self.stack.addWidget(self.statspage)   # index 1
        self.stack.addWidget(self.calcpage)    # index 2

        self.topbar.back_requested.connect(self.go_back)

        # Buttons on main_page
        main_layout_0 = QVBoxLayout(self.main_page)
        statsbtn = QPushButton("Statistics")
        calcbtn = QPushButton("Calculus")
        statsbtn.setFixedSize(100, 100)
        calcbtn.setFixedSize(100,100)
        button_layout.addWidget(statsbtn, 0, 0)
        button_layout.addWidget(calcbtn, 0, 1)

        # Connections
        statsbtn.clicked.connect(lambda: self.go_to(self.statspage))
        calcbtn.clicked.connect(lambda: self.go_to(self.calcpage))
        
        main_layout_0.addWidget(button_container)

        #########################################################
        ### PAGES NEED TO BE ANNOUNCED HERE TO WORK ELSEWHERE ###
        #########################################################

        # ALL STATS PAGES
        self.descstats = DescStats(self)
        self.stack.addWidget(self.descstats)
        self.corrcovar = CorrCovar(self)
        self.stack.addWidget(self.corrcovar)
        self.inferstats = InferStats(self)
        self.stack.addWidget(self.inferstats)
        self.nonparametric = NonParametric(self)
        self.stack.addWidget(self.nonparametric)


    def go_to(self, page):
        current = self.stack.currentWidget()
        if current is not page:
            self.history.append(current)
            self.stack.setCurrentWidget(page)
            self.update_topbar(page)

    def go_back(self):
        if self.history:
            page = self.history.pop()
            self.stack.setCurrentWidget(page)
            self.update_topbar(page)

    def update_topbar(self, page, name=None):
        name = name or getattr(page, "page_name", page.__class__.__name__)
        self.topbar.title_label.setText(name)
        self.topbar.back_btn.setEnabled(bool(self.history))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("src/style/style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = MainWindow("Mathematical", 800, 800)
    window.show()
    sys.exit(app.exec_())