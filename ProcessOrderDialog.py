from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class ProcessOrderDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/process_order_dialog.ui", self)
        self.setWindowTitle("Xử lý phiếu")
        self.status_box.addItem("Đồng ý", 0)
        self.status_box.addItem("Hủy bỏ", 2)
        
    def status(self):
        return self.status_box.currentData()