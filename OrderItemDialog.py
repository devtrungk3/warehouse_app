from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import uic

class OrderItemDialog(QDialog):
    def __init__(self, data):
        super().__init__()
        uic.loadUi("ui/order_item_dialog.ui", self)
        self.setWindowTitle("Hàng hóa trong phiếu")
        self.prod_table.setRowCount(len(data))
        for index, row in enumerate(data):
            self.prod_table.setItem(index, 0, QTableWidgetItem(str(row[0])))
            self.prod_table.setItem(index, 1, QTableWidgetItem(str(row[1])))
            self.prod_table.setItem(index, 2, QTableWidgetItem(str(row[2])))
            self.prod_table.setItem(index, 3, QTableWidgetItem(str(row[3])))
            self.prod_table.setItem(index, 4, QTableWidgetItem(str(row[4])))
