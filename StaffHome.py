from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QMessageBox
from PyQt5 import uic

from datetime import datetime
from Connector import Connector
from AddProdToOrder import AddProdToOrder
from OrderItemDialog import OrderItemDialog
from PartnerDialog import PartnerDialog
from models.OrderItem import OrderItem
from models.Partner import Partner

class StaffHomeWindow(QMainWindow):
    def __init__(self, parent, userdata):
        super().__init__()
        self.__parent = parent
        uic.loadUi("ui/staff_home.ui", self)
        self.setWindowTitle(f"Tài khoản {userdata.username}")
        self.__userdata = userdata
        self.__conn = Connector('WAREHOUSE')
        self.__conn.connect()
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.on_tab_changed)
        self.load_im_ex_data()
        self.type_box.addItem("Nhập kho", 0)
        self.type_box.addItem("Xuất kho", 1)
        
        self.total_cost.setText("0")
        self.add_prod_btn.clicked.connect(self.show_add_product_dialog)
        self.delete_prod_btn.clicked.connect(self.delete_product)
        self.delete_all_prod_btn.clicked.connect(self.clear_product)
        self.submit_btn.clicked.connect(self.submit_product_table)
        
        self.add_prtn_btn.clicked.connect(self.show_add_partner_dialog)
        self.update_prtn_btn.clicked.connect(self.show_update_partner_dialog)
        self.delete_prtn_btn.clicked.connect(self.delete_partner)
        
        self.im_order_item_btn.clicked.connect(self.show_import_order_item)
        
        self.ex_order_item_btn.clicked.connect(self.show_export_order_item)
        
        self.logout_btn.clicked.connect(self.logout)
    
    def on_tab_changed(self, index):
        current_tab = self.tabWidget.tabText(index)
        match current_tab:
            case "Xuất / Nhập kho":
                self.load_im_ex_data()
            case "Đối tác":
                self.reset_partner_data()
            case "Phiếu nhập kho":
                self.load_import_order_data()
            case "Phiếu xuất kho":
                self.load_export_order_data()
            case "Tài khoản":
                self.load_profile()
                
                
                
                
                
                
                
                

    """

        Export / Import tab
        
    """
    def load_im_ex_data(self):
        data = self.__conn.data_query("SELECT id, name FROM partner")
        self.prtn_box.clear()
        if data:
            partners = {}
            for row in data:
                partners[row[0]] = row[1]
                self.prtn_box.addItem(row[1], row[0])
    
    
    def show_add_product_dialog(self):
        data = self.__conn.data_query("SELECT product.id, name, unit, quantity, export_cost FROM product JOIN inventory ON inventory.product_id = product.id")
        if data:
            products = {}
            for row in data:
                products[row[0]] = (row[1], row[2], row[3], row[4])
            dialog = AddProdToOrder(products, self.type_box.currentData())
            if dialog.exec_()  == QDialog.Accepted:
                row_position = self.prod_table.rowCount()
                self.prod_table.insertRow(row_position)
                self.prod_table.setItem(row_position, 0, QTableWidgetItem(str(dialog.product_id())))
                self.prod_table.setItem(row_position, 1, QTableWidgetItem(dialog.product_name()))
                self.prod_table.setItem(row_position, 2, QTableWidgetItem(dialog.quantity()))
                self.prod_table.setItem(row_position, 3, QTableWidgetItem(dialog.unit_cost()))
                self.prod_table.setItem(row_position, 4, QTableWidgetItem(dialog.unit()))
                
                self.total_cost.setText(str(int(self.total_cost.text()) + int(dialog.unit_cost()) * int(dialog.quantity())))
        
    def delete_product(self):
        selected_row = self.prod_table.currentRow()
        if selected_row >= 0 and self.prod_table.item(selected_row, 3):
            self.total_cost.setText(str(int(self.total_cost.text()) - int(self.prod_table.item(selected_row, 2).text()) * int(self.prod_table.item(selected_row, 3).text())))
            self.prod_table.removeRow(selected_row)
            
    def clear_product(self):
        reply = QMessageBox.question(
            self,
            "Xác nhận xóa",
            "Bạn có chắc chắn muốn xóa toàn bộ?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.prod_table.clearContents()
            self.prod_table.setRowCount(0)
            self.total_cost.setText("0")
            
    def submit_product_table(self):
        if (self.prod_table.rowCount() != 0):
            reply = QMessageBox.question(self, "Xác nhận", f"Bạn có chắc chắn muốn yêu cầu {self.type_box.currentText()}?",QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                rows = self.prod_table.rowCount()
                cols = self.prod_table.columnCount()
                queries = ["INSERT INTO [order] (partner_id, type, total_cost, status, staff_id) OUTPUT INSERTED.id VALUES (?,?,?,?,?)"]
                params = [(self.prtn_box.currentData(), self.type_box.currentData(), self.total_cost.text(), 1, self.__userdata.id)]
                
                queries.append("INSERT INTO order_item (product_id, quantity, unit_cost, unit, order_id) VALUES (?,?,?,?,?)")
                for row in range(rows):
                    row_data = []
                    for col in range(cols):
                        item = self.prod_table.item(row, col)
                        if item is not None:
                            row_data.append(item.text())
                    params.append([row_data[0], row_data[2], row_data[3], row_data[4]])
                if self.__conn.manipulate_get_manipulate(queries, params):
                    QMessageBox.information(self, "Thành công", "Yêu cầu thành công")
                    self.prod_table.clearContents()
                    self.prod_table.setRowCount(0)
                else:
                    QMessageBox.warning(self, "Lỗi", "Yêu cầu thất bại")
        
        
        
        
        
        
        
        
        
    """

        Partner tab
        
    """
    def load_partner_data(self):
        if self.__partners:
            self.prtn_table.setRowCount(len(self.__partners))
            for index, partner in enumerate(self.__partners):
                self.prtn_table.setItem(index, 0, QTableWidgetItem(str(partner.id)))
                self.prtn_table.setItem(index, 1, QTableWidgetItem(partner.name))
                self.prtn_table.setItem(index, 2, QTableWidgetItem(partner.description))
        else:
            self.prtn_table.clearContents()
            self.prtn_table.setRowCount(0)
            
    def reset_partner_data(self):
        data = self.__conn.data_query("SELECT id, name, description FROM partner")
        if data:
            self.__partners = [Partner(*row) for row in data]
        else:
            self.__partners = None
        self.load_partner_data()
        
        
    def show_add_partner_dialog(self):
        dialog = PartnerDialog()
        if dialog.exec_() == QDialog.Accepted:
            if self.__conn.data_manipulation("INSERT INTO partner (name, description) VALUES (?,?)", (dialog.partner_name(), dialog.description())):
                QMessageBox.information(self, "Thành công", "Thêm thành công")
                self.reset_partner_data()
            else:
                QMessageBox.warning(self, "Lỗi", "Thêm thất bại")
    
    def show_update_partner_dialog(self):
        selected  = self.prtn_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.prtn_table.item(row, 0).text()
            dialog = PartnerDialog()
            if dialog.exec_() == QDialog.Accepted:
                if self.__conn.data_manipulation("UPDATE partner SET name = ?, description = ? WHERE id = ?", (dialog.partner_name(), dialog.description(), id)):
                    QMessageBox.information(self, "Thành công", "Cập nhật thành công")
                    self.reset_partner_data()
                else:
                    QMessageBox.warning(self, "Lỗi", "Cập nhật thất bại")
        
    def delete_partner(self):
        selected  = self.prtn_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.prtn_table.item(row, 0).text()
            name = self.prtn_table.item(row, 1).text()
            reply = QMessageBox.question(self, "Xác nhận", f"Bạn có chắc chắn muốn xóa đối tác {name}?",QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                if self.__conn.data_manipulation("DELETE FROM partner WHERE id = ?", (id,)):
                    QMessageBox.information(self, "Thành công", "Xóa thành công")
                    self.reset_partner_data()
                else:
                    QMessageBox.warning(self, "Lỗi", "Xóa thất bại")
        
        
        
        
        
        
        
        
        
    """

        Import order tab

    """
    def load_import_order_data(self):
        data = self.__conn.data_query("SELECT [order].id, partner.name, status, total_cost, order_date FROM [order] JOIN partner ON partner.id = [order].partner_id WHERE staff_id = ? AND type = 0 ORDER BY order_date DESC", (self.__userdata.id,))
        
        if data:
            self.import_table.setRowCount(len(data))  
            for index, row in enumerate(data):
                self.import_table.setItem(index, 0, QTableWidgetItem(str(row[0])))
                self.import_table.setItem(index, 1, QTableWidgetItem(row[1]))
                    
                if row[2] == 0:
                    self.import_table.setItem(index, 2, QTableWidgetItem("Đồng ý"))
                elif row[2] == 1:
                    self.import_table.setItem(index, 2, QTableWidgetItem("Chờ duyệt"))
                else:
                    self.import_table.setItem(index, 2, QTableWidgetItem("Hủy bỏ"))
                
                self.import_table.setItem(index, 3, QTableWidgetItem(str(row[3])))
                self.import_table.setItem(index, 4, QTableWidgetItem(str(row[4].strftime("%Y-%m-%d %H:%M:%S"))))
        else:
            self.import_table.clearContents()
            self.import_table.setRowCount(0)
    
    def show_import_order_item(self):
        selected  = self.import_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.import_table.item(row, 0).text()
            data = self.__conn.data_query("SELECT product_id, product.name, quantity, unit_cost, order_item.unit FROM order_item JOIN product ON product.id = order_item.product_id WHERE order_id = ?", (id,))
            if data:
                dialog = OrderItemDialog(data)
                dialog.exec_()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    """

        Export order tab

    """
    def load_export_order_data(self):
        data = self.__conn.data_query("SELECT [order].id, partner.name, status, total_cost, order_date FROM [order] JOIN partner ON partner.id = [order].partner_id WHERE staff_id = ? AND type = 1 ORDER BY order_date DESC", (self.__userdata.id,))
        
        if data:
            self.export_table.setRowCount(len(data))  
            for index, row in enumerate(data):
                self.export_table.setItem(index, 0, QTableWidgetItem(str(row[0])))
                self.export_table.setItem(index, 1, QTableWidgetItem(row[1]))
                    
                if row[2] == 0:
                    self.export_table.setItem(index, 2, QTableWidgetItem("Đồng ý"))
                elif row[2] == 1:
                    self.export_table.setItem(index, 2, QTableWidgetItem("Chờ duyệt"))
                else:
                    self.export_table.setItem(index, 2, QTableWidgetItem("Hủy bỏ"))
                    
                self.export_table.setItem(index, 3, QTableWidgetItem(str(row[3])))
                self.export_table.setItem(index, 4, QTableWidgetItem(str(row[4].strftime("%Y-%m-%d %H:%M:%S"))))
        else:
            self.export_table.clearContents()
            self.export_table.setRowCount(0)
    
    def show_export_order_item(self):
        selected  = self.export_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.export_table.item(row, 0).text()
            data = self.__conn.data_query("SELECT product_id, product.name, quantity, unit_cost, order_item.unit FROM order_item JOIN product ON product.id = order_item.product_id WHERE order_id = ?", (id,))
            if data:
                dialog = OrderItemDialog(data)
                dialog.exec_()
        
        
        
        
        
        
        
        
        
        
        
        
    """
    
        Profile tab
    
    """
    def load_profile(self):
        self.username_input.setText(self.__userdata.username)
        self.fullname_input.setText(self.__userdata.fullname)
        
        
        
    
    
    def logout(self):
        self.close()
        self.__parent.show()