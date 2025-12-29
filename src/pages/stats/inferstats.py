from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QLabel, QPushButton
)
from PyQt5.QtCore import Qt
from src.functions.math.stats import (
    ConfInt, OneSampT, TwoSampT,
    WelchSW, PooledStd, Cohens
)
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
        self.xmu    = QLineEdit()
        self.ymu    = QLineEdit()

        self.x_edit.setPlaceholderText("Input X data:")
        self.y_edit.setPlaceholderText("Input Y Data:")
        self.z_val.setPlaceholderText("Confidence Level (%) (default: 95):")
        self.xmu.setPlaceholderText("X Assumed Mean (\u03BC):")
        self.ymu.setPlaceholderText("Y Assumed Mean (\u03BC):")
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
        self.x_t_test    = QLabel()
        self.y_t_test    = QLabel()
        self.twosampt    = QLabel()
        self.welchsw     = QLabel()
        self.pooled      = QLabel()
        self.cohens      = QLabel()

        self.ci_x_upper.setText("Upper CI X:")
        self.ci_x_lower.setText("Lower CI X:")
        self.ci_y_upper.setText("Upper CI Y:")
        self.ci_y_lower.setText("Lower CI Y:")
        self.x_t_test.setText("X One-Sample T-Test:")
        self.y_t_test.setText("Y One-Sample T-Test:")
        self.twosampt.setText("Two-Sample T-Test:")
        self.welchsw.setText("Welch's Degrees of Freedom(df):")
        self.pooled.setText("Pooled Standard Deviation (Sp):")
        self.cohens.setText("Cohens (d):")

        ##############
        ### LAYOUT ###
        ##############

        #-----------
        # Inputs
        #-----------
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.z_val)

        #-----------
        # left_panel
        #-----------
        left_panel = QVBoxLayout()
        left_panel.addWidget(self.x_edit)
        left_panel.addWidget(self.xmu)
        left_panel.addWidget(self.ci_x_upper)
        left_panel.addWidget(self.ci_x_lower)
        left_panel.addWidget(self.x_t_test)
        #------------
        # right_panel
        #------------
        right_panel = QVBoxLayout()
        right_panel.addWidget(self.y_edit)
        right_panel.addWidget(self.ymu)
        right_panel.addWidget(self.ci_y_upper)
        right_panel.addWidget(self.ci_y_lower)
        right_panel.addWidget(self.y_t_test)


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
        container_layout.addWidget(self.twosampt, alignment=Qt.AlignHCenter)
        container_layout.addWidget(self.welchsw, alignment=Qt.AlignHCenter)
        container_layout.addWidget(self.pooled, alignment=Qt.AlignHCenter)
        container_layout.addWidget(self.cohens, alignment=Qt.AlignHCenter)
        container_layout.addWidget(submit)

        #------------
        # main_layout
        #------------
        main_layout.addWidget(container)

    def updateAll(self):
        xlabel      = self.x_edit.text()
        ylabel      = self.y_edit.text()
        z_val_text  = self.z_val.text()
        x_mu_text   = self.xmu.text()
        y_mu_text   = self.ymu.text()

        
        x_mu    = float(x_mu_text) if x_mu_text.strip() else 0.0
        y_mu    = float(y_mu_text) if y_mu_text.strip() else 0.0
        z_val   = z_val_text if z_val_text.strip() else 95
        if not xlabel:
            self.x_edit.setPlaceholderText("Please Enter X Values")
            return
        if not ylabel:
            self.y_edit.setPlaceholderText("Please Enter Y Values")
            return
        if not z_val:
            self.z_val.setPlaceholderText("Please enter Confidence Level")
            return

        x_arr   = list(map(float, xlabel.split()))
        y_arr   = list(map(float, ylabel.split()))

        ci_lower_x, ci_upper_x, ci_lower_y, ci_upper_y = ConfInt(z_val, x_arr, y_arr)
        x_t, y_t = OneSampT(x_mu, y_mu, x_arr, y_arr)
        t = TwoSampT(x_arr, y_arr)
        df = WelchSW(x_arr, y_arr)
        sp = PooledStd(x_arr, y_arr)
        d = Cohens(x_arr, y_arr, sp)

    

        self.ci_x_upper.setText(f"CI Upper X: {ci_upper_x}")
        self.ci_x_lower.setText(f"CI Lower X: {ci_lower_x}")
        self.ci_y_upper.setText(f"CI Upper Y: {ci_upper_y}")
        self.ci_y_lower.setText(f"CI Lower Y: {ci_lower_y}")
        self.x_t_test.setText(f"X One-Sample T-Test: {x_t}")
        self.y_t_test.setText(f"Y One-Samp T-Test: {y_t}")
        self.twosampt.setText(f"Two-Samp T-Test: {t}")
        self.welchsw.setText(f"Welch's Degrees of Freedom(df): {df}")
        self.pooled.setText(f"Pooled Standard Deviation: {sp}")
        self.cohens.setText(f"Cohends (d): {d}")