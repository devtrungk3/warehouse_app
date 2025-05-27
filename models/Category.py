class Category:
    def __init__(self, id, name, created_at=None):
        self.__id = id
        self.__name = name
        self.__created_at = created_at

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def created_at(self):
        return self.__created_at

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at
        
    