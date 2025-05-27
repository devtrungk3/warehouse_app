from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class CategoryDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/category_dialog.ui", self)
        self.setWindowTitle("Danh mục")
        self.btn_box.setEnabled(False)
        self.name_input.textChanged.connect(self.validate)

    def validate(self):
        self.btn_box.setEnabled(self.name_input.text() != "")

    def get_data(self):
        return self.name_input.text()