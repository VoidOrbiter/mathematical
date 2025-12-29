from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QLabel, QPushButton
)
from PyQt5.QtCore import Qt
from src.functions.math.stats import ConfInt
class InferStats(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.page_name = "Inferential Statistics"

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        container = QWidget()
        container.setFixedWidth(400)
        container_layout = QVBoxLayout()
        container_layout.setSpacing(10)
        container.setLayout(container_layout)

        ###############
        ### WIDGETS ###
        ###############

        #------------
        # Inputs
        #------------
        self.x_edit = QLineEdit()
        self.y_edit = QLineEdit()
        self.z_val  = QLineEdit()
        self.x_edit.setPlaceholderText("Input X data:")
        self.y_edit.setPlaceholderText("Input Y Data:")
        self.z_val.setPlaceholderText("Confidence Level(%):")
        
        #-----------------
        # Calculate Button
        #-----------------
        submit = QPushButton("Calculate")
        submit.clicked.connect(self.updateAll)

        #-------
        # Labels
        #-------
        self.ci_x_upper  = QLabel()
        self.ci_x_lower  = QLabel()
        self.ci_y_upper  = QLabel()
        self.ci_y_lower  = QLabel()

        self.ci_x_upper.setText("Upper CI X:")
        self.ci_x_lower.setText("Lower CI X:")
        self.ci_y_upper.setText("Upper CI Y:")
        self.ci_y_lower.setText("Lower CI Y:")

        ##############
        ### LAYOUT ###
        ##############

        #-----------
        # Inputs
        #-----------
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.x_edit)
        input_layout.addWidget(self.y_edit)
        input_layout.addWidget(self.z_val)

        #-----------
        # left_panel
        #-----------
        left_panel = QVBoxLayout()
        left_panel.addWidget(self.ci_x_upper)
        left_panel.addWidget(self.ci_x_lower)

        #------------
        # right_panel
        #------------
        right_panel = QVBoxLayout()
        right_panel.addWidget(self.ci_y_upper)
        right_panel.addWidget(self.ci_y_lower)

        #-------------
        # panel_parent
        #-------------
        panel_parent = QHBoxLayout()
        panel_parent.addLayout(left_panel)
        panel_parent.addLayout(right_panel)


        #-----------------
        # container_layout
        #-----------------
        container_layout.addLayout(input_layout)
        container_layout.addLayout(panel_parent)
        container_layout.addWidget(submit)

        #------------
        # main_layout
        #------------
        main_layout.addWidget(container)

    def updateAll(self):
        xlabel  = self.x_edit.text()
        ylabel  = self.y_edit.text()
        z_val  = self.z_val.text()

        x_arr   = list(map(float, xlabel.split()))
        y_arr   = list(map(float, ylabel.split()))

        ci_lower_x, ci_upper_x, ci_lower_y, ci_upper_y = ConfInt(z_val, x_arr, y_arr)

        self.ci_x_upper.setText(f"CI Upper X: {ci_upper_x}")
        self.ci_x_lower.setText(f"CI Lower X: {ci_lower_x}")
        self.ci_y_upper.setText(f"CI Upper Y: {ci_upper_y}")
        self.ci_y_lower.setText(f"CI Lower Y: {ci_lower_y}")