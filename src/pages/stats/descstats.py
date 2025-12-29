from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QSizePolicy
)
from scipy import stats
from PyQt5.QtCore import Qt
import numpy as np

class DescStats(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.page_name = "Descriptive Statistics"

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Container widget to confine everything
        container = QWidget()
        container.setFixedWidth(400)  # fixed width to confine layout
        container_layout = QVBoxLayout()
        container_layout.setSpacing(10)
        container.setLayout(container_layout)

        # -------------------
        # Widgets
        # -------------------
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter sample: ")
        self.line_edit.setFixedHeight(25)
        self.line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.rnd = QLineEdit()
        self.rnd.setPlaceholderText("Enter Round: ")
        self.rnd.setFixedHeight(25)

        submit = QPushButton("Calculate")
        submit.setFixedHeight(25)
        submit.clicked.connect(self.calculateAll)

        # Labels
        self.mean_label = QLabel("Mean")
        self.median_label = QLabel("Median")
        self.mode_label = QLabel("Mode")
        self.max_label = QLabel("Max")
        self.min_label = QLabel("Min")
        self.range_label = QLabel("Range")
        self.standerr_label = QLabel("SE: ")
        self.sstdev_label = QLabel("Sample STD: ")
        self.stdev_label = QLabel("Population STD: ")
        self.iqr_label = QLabel("Interpolated IQR")
        self.tukey_label = QLabel("Tukey's Median-Of-Halves IQR")

        # Fix label sizes to keep alignment
        for lbl in [
            self.mean_label, self.median_label, self.mode_label,
            self.max_label, self.min_label, self.range_label,
            self.stdev_label, self.iqr_label, self.tukey_label,
            self.sstdev_label, self.standerr_label
        ]:
            lbl.setFixedHeight(25)
            lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # -------------------
        # Layout rows
        # -------------------
        row1 = QHBoxLayout()
        row1.addWidget(self.mean_label)
        row1.addWidget(self.median_label)
        row1.addWidget(self.mode_label)

        row2 = QHBoxLayout()
        row2.addWidget(self.max_label)
        row2.addWidget(self.min_label)
        row2.addWidget(self.range_label)

        row3 = QHBoxLayout()
        row3.addWidget(self.rnd)
        row3.addWidget(self.standerr_label)
        
        row4 = QHBoxLayout()
        row4.addWidget(self.stdev_label)
        row4.addWidget(self.sstdev_label)

        row5 = QHBoxLayout()
        row5.addWidget(self.iqr_label)
        row5.addWidget(self.tukey_label)

        row6 = QHBoxLayout()
        row6.addWidget(submit, alignment=Qt.AlignCenter)

        # Add everything to container layout
        container_layout.addWidget(self.line_edit)
        container_layout.addLayout(row1)
        container_layout.addLayout(row2)
        container_layout.addLayout(row3)
        container_layout.addLayout(row4)
        container_layout.addLayout(row5)
        container_layout.addLayout(row6)

        # Add container to main layout
        main_layout.addWidget(container, alignment=Qt.AlignTop | Qt.AlignHCenter)

        # Optional: push everything to top
        main_layout.addStretch()


    def calculateAll(self):
        input_text          = self.line_edit.text()

        if not input_text:
            self.line_edit.setPlaceholderText("Please Enter Numbers!")
            return
            
        rnd = self.rnd.text()

        try:
            arr                 = list(map(float, input_text.split()))
        except ValueError:
            self.line_edit.setText("")
            self.line_edit.setPlaceholderText("Please Enter A Valid Number")
            return
            
        self.mean           = np.mean(arr)
        self.median         = np.median(arr)

        self.mode_result    = stats.mode(arr)
        self.mode_val       = self.mode_result.mode.item()
        self.mode_count     = self.mode_result.count.item()

        self.max_val        = np.max(arr)
        self.min_val        = np.min(arr)
        self.range_val      = self.max_val - self.min_val

        self.std_dev        = np.std(arr)
        self.sstd_dev       = np.std(arr, ddof=1)
        arr_sq              = np.sqrt(len(arr))
        self.standerr       = self.std_dev / arr_sq
        
        Q1                  = np.percentile(arr, 25)
        Q3                  = np.percentile(arr, 75)
        self.iqr            = Q3 - Q1

        tukey_iqr_val, Q1_tukey, Q3_tukey = self.tukey_iqr(arr)

        self.median_label.setText(f"Median: {self.median}")
        if self.mode_count  == 1:
            self.mode_label.setText("Mode: No Mode")
        else:
            self.mode_label.setText(f"Mode: {self.mode_val}")
        self.max_label.setText(f"Max: {self.max_val}")
        self.min_label.setText(f"Min: {self.min_val}")
        self.range_label.setText(f"Range: {self.range_val}")

        if not rnd:
            self.stdev_label.setText(f"Population STD: {self.std_dev}")
            self.sstdev_label.setText(f"Sample STD: {self.sstd_dev}")
            self.standerr_label.setText(f"SE: {self.standerr}")
            self.iqr_label.setText(f"IQR: {self.iqr}")
            self.tukey_label.setText(f"Tukey IQR: {tukey_iqr_val}")
            self.mean_label.setText(f"Mean: {self.mean}")
        else:
            try:
                intrnd          = int(rnd)
            except ValueError:
                self.rnd.setText("")
                self.rnd.setPlaceholderText("Enter Number")
                return
            intrnd          = int(rnd)
            std_rnd         = round(self.std_dev, intrnd)
            sstd_rnd        = round(self.sstd_dev, intrnd)
            intiqr          = float(self.iqr)
            iqr_rnd         = round(intiqr, intrnd)
            tukey_iqr_rnd   = round(tukey_iqr_val, intrnd)
            mean_rnd        = round(self.mean, intrnd)
            standerr_rnd    = round(self.standerr, intrnd)
            self.sstdev_label.setText(f"Sample STD: {sstd_rnd}")
            self.stdev_label.setText(f"Population STD: {std_rnd}")
            self.standerr_label.setText(f"SE: {standerr_rnd}")
            self.iqr_label.setText(f"IQR: {iqr_rnd}")
            self.tukey_label.setText(f"Tukey IQR: {tukey_iqr_rnd}")
            self.mean_label.setText(f"Mean: {mean_rnd}")


    def tukey_iqr(self, arr):
        sorted_arr          = sorted(arr)
        n                   = len(sorted_arr)

        if n % 2            == 0:
            median          = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
            lower_half      = sorted_arr[:n//2]
            upper_half      = sorted_arr[n//2:]
        else:
            median          = sorted_arr[n//2]
            lower_half      = sorted_arr[:n//2]
            upper_half      = sorted_arr[n//2 + 1:]

        Q1                  = np.median(lower_half)
        Q3                  = np.median(upper_half)

        iqr                 = Q3 - Q1
        return iqr, Q1, Q3