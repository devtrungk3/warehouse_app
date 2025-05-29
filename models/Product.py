class Product:
    def __init__(self, id, name, unit=None, export_cost=None, category_id=None, category_name=None, created_at=None):
        self.__id = id
        self.__name = name
        self.__unit = unit
        self.__export_cost = export_cost
        self.__category_id = category_id
        self.__category_name = category_name
        self.__created_at = created_at

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    
    @property
    def unit(self):
        return self.__unit
    
    @property
    def export_cost(self):
        return self.__export_cost

    @property
    def category_id(self):
        return self.__category_id
    
    @property
    def category_name(self):
        return self.__category_name

    @property
    def created_at(self):
        return self.__created_at

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @unit.setter
    def unit(self, unit):
        self.__unit = unit

    @export_cost.setter
    def export_cost(self, export_cost):
        self.__export_cost = export_cost

    @category_id.setter
    def category_id(self, category_id):
        self.__category_id = category_id
        
    @category_name.setter
    def category_name(self, category_name):
        self.__category_name = category_name

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at