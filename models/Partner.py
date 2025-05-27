class Partner:
    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @description.setter
    def description(self, description):
        self.__description = description
        
    