from PyQt5.QtWidgets import (
    QWidget
)

class NonParametric(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.page_name = "Non-Parametric & Multi-Group Analysis"

        self.inputs =[]

        self.main_layout = QVBoxLayout()

        self.scroll_layout = QVBoxLayout()
        self.main_layout.addLayout(self.scroll_layout)

        self.add_group_field()
        self.add_group_field()

        self.add_btn = QPushButton("+ Add Group")
        self.add_btn.clicked.connect(self.add_group_field)
        self.main_layout.addWidget(self.add_btn)

        self.setLayout(self.main_layout)
    
    def add_group_field(self):
        new_input = QLineEdit()
        new_input.setPlaceholderText(f"Group {len(self.inputs) + 1} data")

        self.scroll_layout.addWidget(new_input)
        self.inputs.append(new_input)

    def calculateAll(self):
        all_groups_data = []

        for field in self.inputs:
            text = field.text()
            if text:
                arr = np.fromstring(text, sep=",")
                all_groups_data.append(arr)

        if len(all_groups_data) >= 2:
            self.run_anova(all_groups_data)
            