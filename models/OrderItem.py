class OrderItem:
    def __init__(self, product_id, product_name, quantity, unit=None, order_id=None):
        self.__id = id
        self.__order_id = order_id
        self.__product_id = product_id
        self.__product_name = product_name
        self.__unit = unit
        self.__quantity = quantity

    @property
    def id(self):
        return self.__id

    @property
    def order_id(self):
        return self.__order_id

    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def product_name(self):
        return self.__product_name
    
    @property
    def unit(self):
        return self.__unit

    @property
    def quantity(self):
        return self.__quantity

    @id.setter
    def id(self, id):
        self.__id = id

    @order_id.setter
    def order_id(self, order_id):
        self.__order_id = order_id

    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id
        
    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = product_name

    @unit.setter
    def unit(self, unit):
        self.__unit = unit

    @quantity.setter
    def quantity(self, quantity):
        if int(quantity) > 0:
            self.__quantity = quantity
