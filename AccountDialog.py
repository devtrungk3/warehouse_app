from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class AccountDialog(QDialog):
    def __init__(self, roles):
        super().__init__()
        uic.loadUi("ui/account_dialog.ui", self)
        self.setWindowTitle("Tài khoản")
        for id, name in roles.items():
            self.role_box.addItem(name, id)
        self.btn_box.setEnabled(False)
        self.username_input.textChanged.connect(self.validate)
        self.fullname_input.textChanged.connect(self.validate)
        self.password_input.textChanged.connect(self.validate)
        
    def validate(self):
        self.btn_box.setEnabled(self.username_input.text() != "" and self.fullname_input.text() != "" and self.password_input.text() != "")

    def username(self):
        return self.username_input.text()
    def fullname(self):
        return self.fullname_input.text()
    def password(self):
        return self.password_input.text()
    def role_id(self):
        return self.role_box.currentData()