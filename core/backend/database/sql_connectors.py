import pymysql
import sqlite3
import psycopg2
from .abstract_sql_connector import AbstractConnector

class MySQLConnector(AbstractConnector):
    def __init__(self, datastore):
        AbstractConnector.__init__(self, datastore)
        self._datastore = datastore[10:]
        con_str_list = self._datastore.split(':')
        self._user = con_str_list[0]
        con_str_list = con_str_list[1].split('@')
        self._password = con_str_list[0]
        con_str_list = con_str_list[1].split('/')
        self._host = con_str_list[0]
        self._db = con_str_list[1]
        self._cursor = None

    def connect(self):
        try:
            self.connection = pymysql.connect(host=self._host,
                                              user=self._user,
                                              password=self._password,
                                              db=self._db,
                                              charset='utf8mb4')
            print("MySQL database connected.")
            return True
        except Exception as e:
            print(f'Connection error: {str(e)}')
            return False

    def execute(self, query):
        result = None
        if self._cursor is not None:
            try:
                result = self._cursor.execute(query)
            except Exception as e:
                self.connection.rollback()
                print(f'Query execution error: {str(e)}')
        else:
            print("Use start_transaction() first.")
        return result

    def start_transaction(self):
        if self._cursor is None and self.connection is not None:
            self._cursor = self.connection.cursor()

    def end_transaction(self):
        if self.connection is not None and self._cursor is not None:
            self.connection.commit()
            self._cursor.close()
            self._cursor = None

    def close(self):
        self.connection.close()
        self.connection = None
        
        
class SQLiteConnector(AbstractConnector):
    def __init__(self, datastore : str):
        AbstractConnector.__init__(self, datastore)
        self._datastore = datastore[10:]
        self._cursor = None
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(self._datastore)
            print("SQLite database connected.")
            return True
        except Exception as e:
            print(f'Connection error: {str(e)}')
            return False
    
    def execute(self, query):
        result = None
        if self._cursor is not None:
            try:
                result = self._cursor.execute(query)
            except Exception as e:
                self.connection.rollback()
                print(f'Query execution error: {str(e)}')
        else:
            print("Use start_transaction() first.")
        return result
    
    def start_transaction(self):
        if self._cursor is None and self.connection is not None:
            self._cursor = self.connection.cursor()
        else:
            print(self.connection)

    def end_transaction(self):
        if self.connection is not None and self._cursor is not None:
            self.connection.commit()
            self._cursor.close()
            self._cursor = None

    def close(self):
        self.connection.close()
        self.connection = None



class PostgreSQLConnector(AbstractConnector):
    def __init__(self, datastore : str):
        AbstractConnector.__init__(self, datastore)
        self._datastore = datastore[13:]
        self._cursor = None
    
    def connect(self):
        try:
            self.connection = pymysql.connect(host=self._host,
                                              user=self._user,
                                              password=self._password,
                                              dbname=self._db,)
            print("SQLite database connected.")
            return True
        except Exception as e:
            print(f'Connection error: {str(e)}')
            return False
    
    def execute(self, query):
        result = None
        if self._cursor is not None:
            try:
                result = self._cursor.execute(query)
            except Exception as e:
                self.connection.rollback()
                print(f'Query execution error: {str(e)}')
        else:
            print("Use start_transaction() first.")
        return result
    
    def start_transaction(self):
        if self._cursor is None and self.connection is not None:
            self._cursor = self.connection.cursor()
        else:
            print(self.connection)

    def end_transaction(self):
        if self.connection is not None and self._cursor is not None:
            self.connection.commit()
            self._cursor.close()
            self._cursor = None

    def close(self):
        self.connection.close()
        self.connection = None