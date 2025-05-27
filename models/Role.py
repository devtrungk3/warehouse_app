class Role:
    def __init__(self, name, id=None):
        self.__id = id
        self.__name = name


    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name


    @id.setter
    def id(self, id):
        self.__id = id
    @name.setter
    def username(self, name):
        self.__name = name
