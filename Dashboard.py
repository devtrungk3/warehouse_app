from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QMessageBox, QWidget, QVBoxLayout, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
from matplotlib.figure import Figure
from PyQt5 import uic
from AccountDialog import AccountDialog
from Connector import Connector
from CategoryDialog import CategoryDialog
from OrderItemDialog import OrderItemDialog
from PartnerDialog import PartnerDialog
from ProcessOrderDialog import ProcessOrderDialog
from ProductDialog import ProductDialog
from models.Account import Account
from models.Partner import Partner
from models.Product import Product
from models.Category import Category


class DashboardWindow(QMainWindow):
    def __init__(self, parent, userdata):
        super().__init__()
        self.__parent = parent
        uic.loadUi("ui/dashboard.ui", self)
        self.setWindowTitle(f"Quản trị {userdata.username}")
        self.__conn = Connector('WAREHOUSE')
        self.__conn.connect()
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.on_tab_changed)
        
        self.load_dashboard_data()
    
        self.add_cate_btn.clicked.connect(self.show_add_category_dialog)
        self.update_cate_btn.clicked.connect(self.show_update_category_dialog)
        self.delete_cate_btn.clicked.connect(self.delete_category)
        self.search_cate_btn.clicked.connect(self.search_category)
        
        self.add_prod_btn.clicked.connect(self.show_add_product_dialog)
        self.update_prod_btn.clicked.connect(self.show_update_product_dialog)
        self.delete_prod_btn.clicked.connect(self.delete_product)
        self.search_prod_btn.clicked.connect(self.search_product)
        
        self.add_prtn_btn.clicked.connect(self.show_add_partner_dialog)
        self.update_prtn_btn.clicked.connect(self.show_update_partner_dialog)
        self.delete_prtn_btn.clicked.connect(self.delete_partner)
        
        self.im_order_item_btn.clicked.connect(self.show_import_order_item)
        self.process_im_btn.clicked.connect(self.process_import_order)
        self.filter_im_status_box.addItem("Tất cả", -1)
        self.filter_im_status_box.addItem("Đồng ý", 0)
        self.filter_im_status_box.addItem("Chờ duyệt", 1)
        self.filter_im_status_box.addItem("Hủy bỏ", 2)
        self.filter_im_status_box.currentIndexChanged.connect(self.load_import_order_data)
        self.excel_im_btn.clicked.connect(self.to_excel_import)

        self.ex_order_item_btn.clicked.connect(self.show_export_order_item)
        self.process_ex_btn.clicked.connect(self.process_export_order)
        self.filter_ex_status_box.addItem("Tất cả", -1)
        self.filter_ex_status_box.addItem("Đồng ý", 0)
        self.filter_ex_status_box.addItem("Chờ duyệt", 1)
        self.filter_ex_status_box.addItem("Hủy bỏ", 2)
        self.filter_ex_status_box.currentIndexChanged.connect(self.load_export_order_data)
        self.excel_ex_btn.clicked.connect(self.to_excel_export)
        
        self.add_acc_btn.clicked.connect(self.show_add_account_dialog)
        self.update_acc_btn.clicked.connect(self.show_update_account_dialog)
        self.delete_acc_btn.clicked.connect(self.delete_account)
        
        self.logout_btn.clicked.connect(self.logout)
    
    def on_tab_changed(self, index):
        current_tab = self.tabWidget.tabText(index)
        match current_tab:
            case "Tổng quan kho":
                self.load_dashboard_data()
            case "Kho":
                self.load_inventory() 
            case "Danh mục":
                self.reset_category_data()
            case "Hàng hóa":
                self.reset_product_data()
            case "Đối tác":
                self.reset_partner_data()
            case "Phiếu nhập kho":
                self.load_import_order_data()
            case "Phiếu xuất kho":
                self.load_export_order_data()
            case "Tài khoản":
                self.reset_account_data()
    
    
    
    
    
    
    
    
    """
    
        Dashboard tab
        
    """    
    def load_dashboard_data(self):
        
        self.clear_container(self.container1)
        self.clear_container(self.container2)
        self.clear_container(self.container3)
        self.clear_container(self.container4)
        
        data1 = self.__conn.data_query("SELECT TOP 3 product.name, quantity FROM inventory JOIN product ON product.id = inventory.product_id ORDER BY quantity DESC")
        data2 = self.__conn.data_query("SELECT TOP 3 product.name, quantity FROM inventory JOIN product ON product.id = inventory.product_id ORDER BY quantity ASC")
        data3 = self.__conn.data_query("SELECT MONTH(order_date), SUM(total_cost) FROM [order] WHERE type = 0 AND status = 0 AND YEAR(order_date) = YEAR(GETDATE()) GROUP BY MONTH(order_date)")
        data4 = self.__conn.data_query("SELECT MONTH(order_date), SUM(total_cost) FROM [order] WHERE type = 1 AND status = 0 AND YEAR(order_date) = YEAR(GETDATE()) GROUP BY MONTH(order_date)")
        data5 = self.__conn.data_query("SELECT category.name, count(product.id) FROM product JOIN category ON category.id = product.category_id GROUP BY category.name")
        
        if data1:
            self.chart_highest_quantity_prod(data1)
        if data2:
            self.chart_lowest_quantity_prod(data2)
        if data3:
            self.chart_im_ex_inyear(data3, data4)
        if data5:
            self.chart_product_category(data5)
            
        
        
        
    def chart_highest_quantity_prod(self, data):
        labels = []
        values = []
        for row in data:
            labels.append(row[0])
            values.append(row[1])

        fig = Figure(figsize=(4, 3))
        ax = fig.add_subplot()
        ax.bar(labels, values, color='skyblue')
        ax.set_title("Hàng hóa số lượng cao nhất")
        
        canvas = FigureCanvas(fig)
        
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.container1.setLayout(layout)
        
    def chart_lowest_quantity_prod(self, data):
        labels = []
        values = []
        for row in data:
            labels.append(row[0])
            values.append(row[1])

        fig = Figure(figsize=(4, 3))
        ax = fig.add_subplot()
        ax.bar(labels, values, color='lightcoral')
        ax.set_title("Hàng hóa số lượng thấp nhất")
        
        canvas = FigureCanvas(fig)
        
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.container2.setLayout(layout)
    
    def chart_im_ex_inyear(self, expense, income):
        labels = []
        income_values = []
        expense_values = []
        j = 0
        z = 0
        for i in range(1, 13):
            if j < len(income) and income[j][0] == i:
                income_values.append(income[j][1]/1000000)
                j += 1
            else:
                income_values.append(0)
            if z < len(expense) and expense[z][0] == i:
                expense_values.append(expense[z][1]/1000000)
                z += 1
            else:
                expense_values.append(0)
            labels.append(i)


        fig = Figure(figsize=(4, 3))
        ax = fig.add_subplot()
        
        ax.plot(labels, income_values, label='Thu', color='blue', marker='o')
        ax.plot(labels, expense_values, label='Chi', color='green', marker='x')

        ax.set_title("Thu chi trong năm")
        ax.set_xticks(labels)
        ax.set_ylabel('Triệu')
        ax.ticklabel_format(style='plain', axis='y')
        canvas = FigureCanvas(fig)
        
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.container3.setLayout(layout)
        
    def chart_product_category(self, data):
        labels = []
        values = []
        for row in data:
            labels.append(row[0])
            values.append(row[1])


        fig = Figure(figsize=(5, 4))
        ax = fig.add_subplot()

        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title("Mức phân tán danh mục")
        ax.axis('equal') 

        canvas = FigureCanvas(fig)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.container4.setLayout(layout)
        
    def clear_container(self, container):
        if container.layout() is not None:
            old_layout = container.layout()
            while old_layout.count():
                item = old_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
            QWidget().setLayout(old_layout)
    
    
    
    
    
    
    
    
    
    
    """
    
        Inventory tab
    
    """
    def load_inventory(self):
        data = self.__conn.data_query("SELECT product_id, product.name, quantity, updated_at FROM inventory JOIN product ON product.id = inventory.product_id ORDER BY quantity DESC")
        if data:
            self.inven_table.setRowCount(len(data))  
            for index, row in enumerate(data):
                self.inven_table.setItem(index, 0, QTableWidgetItem(str(row[0])))
                self.inven_table.setItem(index, 1, QTableWidgetItem(row[1]))
                self.inven_table.setItem(index, 2, QTableWidgetItem(str(row[2])))
                self.inven_table.setItem(index, 3, QTableWidgetItem(str(row[3].strftime("%Y-%m-%d %H:%M:%S"))))
    
    
    
    
    
    
    
    
    
    
    
        
    """
    
        Category tab
        
    """    
    def load_category_data(self):
        if self.__categories:
            self.cate_table.setRowCount(len(self.__categories))  
            for index, category in enumerate(self.__categories):
                self.cate_table.setItem(index, 0, QTableWidgetItem(str(category.id)))
                self.cate_table.setItem(index, 1, QTableWidgetItem(category.name))
                self.cate_table.setItem(index, 2, QTableWidgetItem(str(category.created_at.strftime("%Y-%m-%d %H:%M:%S"))))
        else:
            self.cate_table.clearContents()
            self.cate_table.setRowCount(0)
            # self.cate_table.model().removeRows(0, self.cate_table.model().rowCount())
            
    def reset_category_data(self):
        data = self.__conn.data_query("SELECT id, name, created_at FROM category")
        if data:
            self.__categories = [Category(*row) for row in data]
        else:
            self.__categories = None
        self.load_category_data()
                
    def show_add_category_dialog(self):
        dialog = CategoryDialog()
        if dialog.exec_() == QDialog.Accepted:
            if self.__conn.data_manipulation("INSERT INTO category (name) VALUES (?)", (dialog.get_data(),)):
                QMessageBox.information(self, "Thành công", "Thêm thành công")
                self.reset_category_data()
            else:
                QMessageBox.warning(self, "Lỗi", "Thêm thất bại")
    
    def show_update_category_dialog(self):
        selected  = self.cate_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.cate_table.item(row, 0).text()
            dialog = CategoryDialog()
            if dialog.exec_() == QDialog.Accepted:
                if self.__conn.data_manipulation("UPDATE category SET name = ? WHERE id = ?", (dialog.get_data(), id)):
                    QMessageBox.information(self, "Thành công", "Cập nhật thành công")
                    self.reset_category_data()
                else:
                    QMessageBox.warning(self, "Lỗi", "Cập nhật thất bại")
        
    def delete_category(self):
        selected  = self.cate_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.cate_table.item(row, 0).text()
            name = self.cate_table.item(row, 1).text()
            reply = QMessageBox.question(self, "Xác nhận", f"Bạn có chắc chắn muốn xóa danh mục {name}?",QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                if self.__conn.data_manipulation("DELETE FROM category WHERE id = ?", (id,)):
                    QMessageBox.information(self, "Thành công", "Xóa thành công")
                    self.reset_category_data()
                else:
                    QMessageBox.warning(self, "Lỗi", "Xóa thất bại")
    
    def search_category(self):
        input = self.search_cate_input.text().strip()
        data = self.__conn.data_query("SELECT id, name, created_at FROM category WHERE name like ?", (f"%{input}%",))
        if data:
            self.__categories = [Category(*row) for row in data]
        else:
            self.__categories = None
        self.load_category_data()
        
        
        
        
        
        
        
        
        
        
        

        
        
    """

        Product tab
            
    """
    def load_product_data(self):
        if self.__products:
            self.prod_table.setRowCount(len(self.__products))  
            for index, product in enumerate(self.__products):
                self.prod_table.setItem(index, 0, QTableWidgetItem(str(product.id)))
                self.prod_table.setItem(index, 1, QTableWidgetItem(product.name))
                self.prod_table.setItem(index, 2, QTableWidgetItem(product.category_name))
                self.prod_table.setItem(index, 3, QTableWidgetItem(product.unit))
                self.prod_table.setItem(index, 4, QTableWidgetItem(str(product.export_cost)))
                self.prod_table.setItem(index, 5, QTableWidgetItem(str(product.created_at.strftime("%Y-%m-%d %H:%M:%S"))))
        else:
            self.prod_table.clearContents()
            self.prod_table.setRowCount(0)
        
    def reset_product_data(self):
        data = self.__conn.data_query("SELECT product.id, product.name, unit, export_cost, category_id, category.name, product.created_at FROM product JOIN category ON product.category_id = category.id")
        if data:
            self.__products = [Product(*row) for row in data]
        else:
            self.__products = None
        self.load_product_data()
        
    def show_add_product_dialog(self):
        data = self.__conn.data_query("SELECT id, name FROM category")
        if data:
            categories = {}
            for row in data:
                categories[row[0]] = row[1]
            dialog = ProductDialog(categories)
            if dialog.exec_()  == QDialog.Accepted:
                product_name = dialog.product_name()
                unit = dialog.unit()
                category_id = dialog.category_id()
                export_cost = dialog.export_cost()
                queries = ["INSERT INTO product (name, unit, export_cost, category_id) OUTPUT INSERTED.id VALUES (?,?,?,?)"]
                params = [(product_name, unit , export_cost, category_id), []]
                queries.append("INSERT INTO inventory (product_id, quantity) VALUES (?,0)")
                if self.__conn.manipulate_get_manipulate(queries, params):
                    QMessageBox.information(self, "Thành công", "Thêm thành công")
                    self.reset_product_data()
                else:
                    QMessageBox.warning(self, "Lỗi", "Thêm thất bại")
    
    def show_update_product_dialog(self):
        selected  = self.prod_table.currentItem()
        if selected:
            data = self.__conn.data_query("SELECT id, name FROM category")
            if data:
                categories = {}
                for row in data:
                    categories[row[0]] = row[1]
                dialog = ProductDialog(categories)
                row  = selected.row()
                id = self.prod_table.item(row, 0).text()
                if dialog.exec_() == QDialog.Accepted:
                    product_name = dialog.product_name()
                    unit = dialog.unit()
                    export_cost = dialog.export_cost()
                    category_id = dialog.category_id()
                    if self.__conn.data_manipulation("UPDATE product SET name = ?, unit = ?, export_cost = ?, category_id = ? WHERE id = ?", (product_name, unit, export_cost, category_id, id)):
                        QMessageBox.information(self, "Thành công", "Cập nhật thành công")
                        self.reset_product_data()
                    else:
                        QMessageBox.warning(self, "Lỗi", "Cập nhật thất bại")
    
    def delete_product(self):
        selected  = self.prod_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.prod_table.item(row, 0).text()
            name = self.prod_table.item(row, 1).text()
            reply = QMessageBox.question(self, "Xác nhận", f"Bạn có chắc chắn muốn xóa hàng hóa {name}?",QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                queries = ["DELETE FROM inventory WHERE product_id = ?", "DELETE FROM product WHERE id = ?"]
                params = [(id,), (id,)]
                if self.__conn.multi_data_manipulation(queries, params):
                    QMessageBox.information(self, "Thành công", "Xóa thành công")
                    self.reset_product_data()
                else:
                    QMessageBox.warning(self, "Lỗi", "Xóa thất bại")
        
    def search_product(self):
        input = self.search_prod_input.text().strip()
        data = self.__conn.data_query("SELECT product.id, product.name, unit, category_id, category.name, product.created_at FROM product JOIN category ON product.category_id = category.id WHERE product.name like ? OR category.name like ? OR unit like ?", (f"%{input}%", f"%{input}%", f"%{input}%"))
        if data:
            self.__products = [Product(*row) for row in data]
        else:
            self.__products = None
        self.load_product_data()
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        query = "SELECT [order].id, partner.name, status, account.username, total_cost, order_date FROM [order] JOIN partner ON partner.id = [order].partner_id JOIN account ON account.id = [order].staff_id WHERE type = 0 "

        params = None
        if self.filter_im_status_box.currentData() >= 0 and self.filter_im_status_box.currentData() <= 2:
            query += "AND status = ? "
            params = (self.filter_im_status_box.currentData(),)
            
        query += "ORDER BY order_date DESC"
            
        data = self.__conn.data_query(query, params)
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
                
                self.import_table.setItem(index, 3, QTableWidgetItem(row[3]))
                self.import_table.setItem(index, 4, QTableWidgetItem(str(row[4])))
                self.import_table.setItem(index, 5, QTableWidgetItem(str(row[5].strftime("%Y-%m-%d %H:%M:%S"))))
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
        
    def process_import_order(self):
        selected  = self.import_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.import_table.item(row, 0).text()
            status = self.import_table.item(row, 2).text()
            if status == "Chờ duyệt":
                dialog = ProcessOrderDialog()
                if dialog.exec_() and QDialog.Accepted:
                    data = self.__conn.data_query("SELECT product_id, quantity FROM order_item WHERE order_id = ?", (id, ))
                    if data:
                        queries = ["UPDATE [order] SET status = ? WHERE id = ?"]
                        params = [(dialog.status(), id)]
                        if dialog.status() == 0:
                            for row in data:
                                queries.append("UPDATE inventory SET quantity = quantity + ?, updated_at = GETDATE() WHERE product_id = ?")
                                params.append((row[1], row[0]))
                        if self.__conn.multi_data_manipulation(queries, params):
                            QMessageBox.information(self, "Thành công", "Cập nhật thành công")
                            self.load_import_order_data()
                        else:
                            QMessageBox.warning(self, "Lỗi", "Cập nhật thất bại")       
    
    def to_excel_import(self):
        data = self.__conn.data_query("SELECT [order].id, partner.name, account.username, total_cost, order_date FROM [order] JOIN partner ON partner.id = [order].partner_id JOIN account ON account.id = [order].staff_id WHERE type = 0 AND status = 0 ORDER BY order_date DESC")
        if data:
            import_orders = []
            for row in data:
                import_orders.append([str(row[0]), row[1], row[2], str(row[3]), str(row[4].strftime("%H:%M:%S %d-%m-%Y"))])
                
            file_path, _ = QFileDialog.getSaveFileName(
                None,
                "Xuất file",
                "phieu_nhap_kho.xlsx",
                "Excel Files (*.xlsx)"
            )

            if not file_path:
                return

            if not file_path.endswith(".xlsx"):
                file_path += ".xlsx"

            df = pd.DataFrame(import_orders, columns=["Mã hóa đơn", "Nhà cung cấp", "Nhân viên phụ trách", "Tổng tiền", "Ngày tạo"])
            df.to_excel(file_path, index=False, engine='openpyxl')
                
        
        
        
        
        
        
        
        
    """

        Export order tab
        
    """
    def load_export_order_data(self):
        query = "SELECT [order].id, partner.name, status, account.username, total_cost, order_date FROM [order] JOIN partner ON partner.id = [order].partner_id JOIN account ON account.id = [order].staff_id WHERE type = 1 "

        params = None
        if self.filter_ex_status_box.currentData() >= 0 and self.filter_ex_status_box.currentData() <= 2:
            query += "AND status = ?"
            params = (self.filter_ex_status_box.currentData(),)
            
        query += " ORDER BY order_date DESC"
            
        data = self.__conn.data_query(query, params)
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
                
                self.export_table.setItem(index, 3, QTableWidgetItem(row[3]))
                self.export_table.setItem(index, 4, QTableWidgetItem(str(row[4])))
                self.export_table.setItem(index, 5, QTableWidgetItem(str(row[5].strftime("%Y-%m-%d %H:%M:%S"))))
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
        
    def process_export_order(self):
        selected  = self.export_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.export_table.item(row, 0).text()
            status = self.export_table.item(row, 2).text()
            if status == "Chờ duyệt":
                dialog = ProcessOrderDialog()
                if dialog.exec_() and QDialog.Accepted:
                    data = self.__conn.data_query("SELECT product_id, quantity from order_item WHERE order_id = ?", (id, ))
                    if data:
                        queries = ["UPDATE [order] SET status = ? WHERE id = ?"]
                        params = [(dialog.status(), id)]
                        if dialog.status() == 0:
                            for row in data:
                                queries.append("UPDATE inventory SET quantity = quantity - ?, updated_at = GETDATE() WHERE product_id = ?")
                                params.append((row[1], row[0]))
                        if self.__conn.multi_data_manipulation(queries, params):
                            QMessageBox.information(self, "Thành công", "Cập nhật thành công")
                            self.load_export_order_data()
                        else:
                            QMessageBox.warning(self, "Lỗi", "Cập nhật thất bại")     
        
    def to_excel_export(self):
        data = self.__conn.data_query("SELECT [order].id, partner.name, account.username, total_cost, order_date FROM [order] JOIN partner ON partner.id = [order].partner_id JOIN account ON account.id = [order].staff_id WHERE type = 1 AND status = 0 ORDER BY order_date DESC")
        if data:
            export_orders = []
            for row in data:
                export_orders.append([str(row[0]), row[1], row[2], str(row[3]), str(row[4].strftime("%H:%M:%S %d-%m-%Y"))])
                
            file_path, _ = QFileDialog.getSaveFileName(
                None,
                "Xuất file",
                "phieu_xuat_kho.xlsx",
                "Excel Files (*.xlsx)"
            )

            if not file_path:
                return

            if not file_path.endswith(".xlsx"):
                file_path += ".xlsx"

            df = pd.DataFrame(export_orders, columns=["Mã hóa đơn", "Nhà cung cấp", "Nhân viên phụ trách", "Tổng tiền", "Ngày tạo"])
            df.to_excel(file_path, index=False, engine='openpyxl')
        
        
        
        
        
        
        
        
        
    """

        Account tab
        
    """
    def load_account_data(self):
        if self.__accounts:
            self.acc_table.setRowCount(len(self.__accounts))  
            for index, account in enumerate(self.__accounts):
                self.acc_table.setItem(index, 0, QTableWidgetItem(str(account.id)))
                self.acc_table.setItem(index, 1, QTableWidgetItem(account.username))
                self.acc_table.setItem(index, 2, QTableWidgetItem(account.fullname))
                self.acc_table.setItem(index, 3, QTableWidgetItem(account.role_name))
                self.acc_table.setItem(index, 4, QTableWidgetItem(str(account.created_at.strftime("%Y-%m-%d %H:%M:%S"))))
        else:
            self.acc_table.clearContents()
            self.acc_table.setRowCount(0)
        
    def reset_account_data(self):
        data = self.__conn.data_query("SELECT account.id, username, fullname, role_id, role.name, created_at FROM account JOIN role ON account.role_id = role.id")
        if data:
            self.__accounts = []
            for row in data:
                self.__accounts.append(Account(id=row[0], username=row[1], fullname=row[2], role_id=row[3], role_name=row[4], created_at=row[5]))
        else:
            self.__accounts = None
        self.load_account_data()
        
    def show_add_account_dialog(self):
        data = self.__conn.data_query("SELECT id, name FROM role WHERE id <> 1")
        if data:
            roles = {}
            for row in data:
                roles[row[0]] = row[1]
            dialog = AccountDialog(roles)
            if dialog.exec_()  == QDialog.Accepted:
                username = dialog.username()
                fullname = dialog.fullname()
                password = dialog.password()
                role_id = dialog.role_id()
                if self.__conn.data_manipulation("INSERT INTO account (username, fullname, password, role_id) VALUES (?,?,?,?)", (username, fullname, password, role_id)):
                    QMessageBox.information(self, "Thành công", "Thêm thành công")
                    self.reset_account_data()
                else:
                    QMessageBox.warning(self, "Lỗi", "Thêm thất bại")
    
    def show_update_account_dialog(self):
        selected  = self.acc_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.acc_table.item(row, 0).text()
            username = self.acc_table.item(row, 1).text()
            data = self.__conn.data_query("SELECT id, name FROM role")
            if username != "admin" and data:
                roles = {}
                for row in data:
                    roles[row[0]] = row[1]
                dialog = AccountDialog(roles)
                if dialog.exec_() == QDialog.Accepted:
                    username = dialog.username()
                    fullname = dialog.fullname()
                    password = dialog.password()
                    role_id = dialog.role_id()
                    if self.__conn.data_manipulation("UPDATE account SET username = ?, password = ?, fullname = ?, role_id = ? WHERE id = ?", (username, password, fullname, role_id, id)):
                        QMessageBox.information(self, "Thành công", "Cập nhật thành công")
                        self.reset_account_data()
                    else:
                        QMessageBox.warning(self, "Lỗi", "Cập nhật thất bại")
    
    def delete_account(self):
        selected  = self.acc_table.currentItem()
        if selected:
            row  = selected.row()
            id = self.acc_table.item(row, 0).text()
            username = self.acc_table.item(row, 1).text()
            if username != "admin":
                reply = QMessageBox.question(self, "Xác nhận", f"Bạn có chắc chắn muốn xóa người dùng {username}?",QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    if self.__conn.data_manipulation("DELETE FROM account WHERE id = ?", (id,)):
                        QMessageBox.information(self, "Thành công", "Xóa thành công")
                        self.reset_account_data()
                    else:
                        QMessageBox.warning(self, "Lỗi", "Xóa thất bại")
                    
                    
            
        
        
        
        
            
            
    def logout(self):
        self.close()
        self.__parent.show()
    