from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class PartnerDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/partner_dialog.ui", self)
        self.setWindowTitle("Đối tác")
        
        self.btn_box.setEnabled(False)
        self.name_input.textChanged.connect(self.validate)

    def validate(self):
        self.btn_box.setEnabled(self.name_input.text() != "")

    def partner_name(self):
        return self.name_input.text()
    
    def description(self):
        return self.desc_input.text()