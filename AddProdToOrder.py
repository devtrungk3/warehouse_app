from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import re
class AddProdToOrder(QDialog):
    def __init__(self, products):
        super().__init__()
        uic.loadUi("ui/add_prod_to_order.ui", self)
        self.setWindowTitle("Nhập kho")
        self.__products = products
        for id, value in products.items():
            self.prod_box.addItem(value[0], id)
        self.unit_input.setText(self.__products[self.prod_box.currentData()][1])
        self.prod_box.currentIndexChanged.connect(self.get_unit)
        self.quantity_input.textChanged.connect(self.validate_quantity)
        self.btn_box.setEnabled(False) 
        
    def validate_quantity(self):
        quantity = self.quantity_input.text().strip()
        if re.fullmatch(r"0*[1-9]\d*", quantity) and int(quantity) <= self.__products[self.prod_box.currentData()][2]:
            self.btn_box.setEnabled(True)
        else:
            self.btn_box.setEnabled(False)
        
    def get_unit(self):
        self.unit_input.setText(self.__products[self.prod_box.currentData()][1])

    def product_id(self):
        return self.prod_box.currentData()
    
    def product_name(self):
        return self.prod_box.currentText()
    
    def unit(self):
        return self.unit_input.text()
    
    def quantity(self):
        return self.quantity_input.text()