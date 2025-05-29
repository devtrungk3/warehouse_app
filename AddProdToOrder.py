from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import re
class AddProdToOrder(QDialog):
    def __init__(self, products, type):
        super().__init__()
        uic.loadUi("ui/add_prod_to_order.ui", self)
        self.setWindowTitle("Nhập kho")
        self.__products = products
        self.__type = type
        for id, value in products.items():
            self.prod_box.addItem(value[0], id)
        self.unit_input.setText(self.__products[self.prod_box.currentData()][1])
        self.prod_box.currentIndexChanged.connect(self.product_onChanged)
        self.quantity_input.textChanged.connect(self.validate)
        self.unit_cost_input.textChanged.connect(self.validate)
        
        if type == 1: 
            self.unit_cost_input.setReadOnly(True)
            self.unit_cost_input.setText(str(self.__products[self.prod_box.currentData()][3]))
        
        self.btn_box.setEnabled(False) 
        
    def validate(self):
        quantity = self.quantity_input.text().strip()
        unit_cost = self.unit_cost_input.text().strip()
        check_cost = unit_cost and re.fullmatch(r"0*[1-9]\d*", unit_cost)
        check_inventory = quantity and (self.__type == 1 and int(quantity) <= self.__products[self.prod_box.currentData()][2]) or self.__type == 0
        if check_cost and quantity and re.fullmatch(r"0*[1-9]\d*", quantity) and check_inventory:
            self.btn_box.setEnabled(True)
        else:
            self.btn_box.setEnabled(False)
        
    def product_onChanged(self):
        self.unit_input.setText(self.__products[self.prod_box.currentData()][1])
        if self.__type == 1:
            self.unit_cost_input.setText(str(self.__products[self.prod_box.currentData()][3]))

    def product_id(self):
        return self.prod_box.currentData()
    
    def product_name(self):
        return self.prod_box.currentText()
    
    def unit(self):
        return self.unit_input.text()
    
    def quantity(self):
        return self.quantity_input.text()
    
    def unit_cost(self):
        return self.unit_cost_input.text()