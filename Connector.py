import pyodbc
import pyodbc

class Connector:
    def __init__(self, database, driver='{ODBC Driver 17 for SQL Server}', server='localhost\SQLEXPRESS'):
        self.__driver = driver
        self.__server = server
        self.__database = database
        
    def connect(self):
        try:
            self.__conn = pyodbc.connect(
                f"DRIVER={self.__driver};"
                f"SERVER={self.__server};"
                f"DATABASE={self.__database};"
                "Trusted_Connection=yes;"
            )
            self.__cursor = self.__conn.cursor()
            return True
        except pyodbc.Error as e:
            print("Connect failed: ", e)
            return False
        
        
    def data_query(self, query, params=None):
        if self.__cursor:
            try:
                if params:
                    self.__cursor.execute(query, params)
                else:
                    self.__cursor.execute(query)
                return self.__cursor.fetchall()
            except pyodbc.Error as e:
                print("Data query failed: ", e)
                return None
            
        print("No active db connection")
        return None
    
    
    def data_manipulation(self, query, params):
        if self.__cursor:
            try:
                self.__cursor.execute(query, params)
                self.__conn.commit()
                return True
            except pyodbc.Error as e:
                print("Data manipulation failed: ", e)
                return False
            
        print("No active db connection")
        return False
    
    
    def manipulate_get_manipulate(self, queries, params):
        if self.__cursor:
            try:
                # Add order
                self.__cursor.execute(queries[0], params[0])
                id = self.__cursor.fetchone()[0]
                params.remove(params[0])
                # Add order_item
                for i in range(0, len(params)):
                    params[i].append(id)
                    params[i] = tuple(params[i])
                self.__cursor.executemany(queries[1], params)
                
                self.__conn.commit()
                return True
            except pyodbc.Error as e:
                self.__conn.rollback()
                print("Data manipulation failed: ", e)
                return False
        print("No active db connection")
        return False
    
    def multi_data_manipulation(self, queries, params):
        if self.__cursor:
            try:
                for i in range(0, len(queries)):
                    self.__cursor.execute(queries[i], params[i])
                self.__conn.commit()
                return True
            except pyodbc.Error as e:
                self.__conn.rollback()
                print("Data manipulation failed: ", e)
                return False
            
        print("No active db connection")
        return False