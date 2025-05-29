from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

from Connector import Connector
from Dashboard import DashboardWindow
from StaffHome import StaffHomeWindow
from models.Account import Account

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)
        self.__conn = Connector('WAREHOUSE')
        self.__conn.connect()
        self.login_button.clicked.connect(self.check_credentials)
        self.setWindowTitle("Quản lý kho")

    def check_credentials(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()
        query = f"SELECT TOP 1 account.id, username, fullname, role_id, role.name  FROM account inner join role on account.role_id = role.id where username = ? and password = ?"
        params = (username, password)
        data = self.__conn.data_query(query, params)
        if data:
            self.__userdata = Account(id=data[0][0], username=data[0][1], fullname=data[0][2], role_id=data[0][3], role_name=data[0][4])
            self.username_input.setText("")
            self.password_input.setText("")
            if self.__userdata.role_id == 1:
                self.open_dashboard()
                self.close()
            elif self.__userdata.role_id == 2:
                self.open_staff_home()
                self.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Thông tin đăng nhập không chính xác")

    def open_dashboard(self):
        self.dashboard = DashboardWindow(self, self.__userdata)
        self.dashboard.show()
    def open_staff_home(self):
        self.staffhome = StaffHomeWindow(self, self.__userdata)
        self.staffhome.show()