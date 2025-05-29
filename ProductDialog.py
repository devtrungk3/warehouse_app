from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import re

class ProductDialog(QDialog):
    def __init__(self, categories):
        super().__init__()
        uic.loadUi("ui/product_dialog.ui", self)
        self.setWindowTitle("Hàng hóa")
        for id, name in categories.items():
            self.cate_box.addItem(name, id)
        self.btn_box.setEnabled(False)
        self.name_input.textChanged.connect(self.validate)
        self.unit_input.textChanged.connect(self.validate)
        self.ex_cost_input.textChanged.connect(self.validate)
        
    def validate(self):
        ex_cost = self.ex_cost_input.text().strip()
        if self.name_input.text() != "" and self.unit_input.text() != "" and ex_cost and re.fullmatch(r"0*[1-9]\d*", ex_cost):
            self.btn_box.setEnabled(True)
        else:
            self.btn_box.setEnabled(False)

    def product_name(self):
        return self.name_input.text()
    
    def unit(self):
        return self.unit_input.text()
    
    def category_id(self):
        return self.cate_box.currentData()
    
    def export_cost(self):
        return self.ex_cost_input.text()