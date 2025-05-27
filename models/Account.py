class Account:
    def __init__(self, id, username, password=None, fullname=None, role_id=None, role_name=None, created_at=None):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__fullname = fullname
        self.__role_id = role_id
        self.__role_name = role_name
        self.__created_at = created_at


    @property
    def id(self):
        return self.__id
    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password
    @property
    def fullname(self):
        return self.__fullname
    @property
    def role_id(self):
        return self.__role_id
    @property
    def role_name(self):
        return self.__role_name
    @property
    def created_at(self):
        return self.__created_at


    @id.setter
    def id(self, id):
        self.__id = id
    @username.setter
    def username(self, username):
        self.__username = username
    @password.setter
    def password(self, password):
        self.__password = password
    @fullname.setter
    def fullname(self, fullname):
        self.__fullname = fullname
    @role_id.setter
    def role_id(self, role_id):
        self.__role_id = role_id
    @role_name.setter
    def role_name(self, role_name):
        self.__role_name = role_name
    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at
