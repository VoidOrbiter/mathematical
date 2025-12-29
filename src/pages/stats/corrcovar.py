from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QSizePolicy, QLineEdit, QLabel,
    QPushButton
)
from PyQt5.QtCore import Qt

import numpy as np
from src.functions.math.stats import (
    Covariance, Pearson, SpearmanCoeff
)
from src.functions.math.plots.scatter import Scatter

class CorrCovar(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.page_name  = "Correlation & Covariance"

        # layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.plot_container = QVBoxLayout()

        # Container widget
        container = QWidget()
        container.setFixedWidth(500)
        container_layout = QVBoxLayout()
        container_layout.setSpacing(10)
        container.setLayout(container_layout)

        rho_ = "\u03C1"

        # X ARRAY INPUT FIELD
        self.x_edit = QLineEdit()
        self.x_edit.setPlaceholderText("Enter X Variables: ")
        self.x_edit.setFixedHeight(25)
        self.x_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Y ARRAY INPUT FIELD
        self.y_edit = QLineEdit()
        self.y_edit.setPlaceholderText("Enter Y Variables: ")
        self.y_edit.setFixedHeight(25)
        self.y_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Rounding input
        self.rnd = QLineEdit()
        self.rnd.setPlaceholderText("Enter Round: ")
        self.rnd.setFixedHeight(70)
        self.rnd.setFixedWidth(100)

        # Table Inputs
        self.x_label = QLineEdit()
        self.x_label.setPlaceholderText("X-Axis Title")
        self.y_label = QLineEdit()
        self.y_label.setPlaceholderText("Y-Axis Label")
        self.title_label = QLineEdit()
        self.title_label.setPlaceholderText("Plot Title")


        submit = QPushButton("Calculate")
        submit.setFixedHeight(25)
        submit.clicked.connect(self.calculateAll)

        # Labels
        self.covar_label = QLabel("Covariance")
        self.r_label = QLabel("Pearsons(r)")
        self.rho_label = QLabel(f"Spearman's {rho_}")

        for lbl in [
            self.covar_label, self.r_label, self.rho_label
        ]:
            lbl.setFixedHeight(25)
            lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Layout

        main_row = QHBoxLayout()
        left_column = QVBoxLayout()
        left_column.addWidget(self.x_edit)
        left_column.addWidget(self.y_edit)

        right_column = QVBoxLayout()
        right_column.addWidget(self.rnd)
        
        row1 = QHBoxLayout()
        row1.addWidget(self.covar_label, alignment=Qt.AlignCenter)
        row1.addWidget(self.covar_label)

        row2 = QHBoxLayout()
        row2.addWidget(self.r_label)
        row2.addWidget(self.rho_label)

        row3 = QHBoxLayout()
        row3.addWidget(self.x_label)
        row3.addWidget(self.y_label)
        row3.addWidget(self.title_label)

        row4 = QHBoxLayout()
        row4.addWidget(submit, alignment=Qt.AlignCenter)


        main_row.addLayout(left_column)
        main_row.addLayout(right_column)

        container_layout.addLayout(main_row)
        container_layout.addLayout(row2)
        container_layout.addLayout(row3)
        container_layout.addLayout(row4)
        container_layout.addLayout(self.plot_container)

        main_layout.addWidget(container, alignment=Qt.AlignTop | Qt.AlignHCenter)

    def calculateAll(self):
        ylabel = self.y_label.text()
        xlabel = self.x_label.text()
        title = self.title_label.text()
        x_text = self.x_edit.text()
        y_text = self.y_edit.text()

        x_arr = list(map(float, x_text.split()))
        y_arr = list(map(float, y_text.split()))

        if not x_text:
            self.x_edit.setPlaceholderText("Please Enter X Values")
            return
        if not y_text:
            self.y_text.setPlaceholderText("Please Enter Y Values")
            return
        
        rnd = self.rnd.text()

        x_dev_list, y_dev_list, product_list, covariance = Covariance(x_arr, y_arr)
        r = Pearson(x_dev_list, y_dev_list, covariance)
        rho = SpearmanCoeff(x_arr, y_arr)
        rho_ = "\u03C1"
        if not rnd:
            self.covar_label.setText(f"Covariance: {covariance}")
            self.r_label.setText(f"Pearsons(r): {r}")
            self.rho_label.setText(f"Spearman's {rho_}: {rho}")
        else:
            try:
                intrnd = int(rnd)
            except ValueError:
                self.rnd.setText("")
                self.rnd.setPlaceholderText("Enter a number")
                return
            covar_float = float(covariance)
            covar_rnd = round(covar_float, intrnd)
            self.covar_label.setText(f"Covariance: {covar_rnd}")
            r_rnd = round(r, intrnd)
            self.r_label.setText(f"Pearsons(r): {r_rnd}")
            rho_float = float(rho)
            rho_rnd = round(rho_float, intrnd)
            self.rho_label.setText(f"Spearman's {rho_}: {rho_rnd}")

        if hasattr(self, 'plot_widget'):
            self.plot_container.removeWidget(self.plot_widget)
            self.plot_widget.setParent(None)
            
        self.plot_widget = Scatter(x_arr, y_arr, x_label=xlabel or 'X', y_label=ylabel or 'Y', title=title or 'Scatter Plot')
        self.plot_widget.setFixedSize(450, 450)
        self.plot_container.addWidget(self.plot_widget, alignment=Qt.AlignCenter)

        