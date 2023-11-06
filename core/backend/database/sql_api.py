from .abstract_sql_connector import AbstractConnector
from .sql_connectors import MySQLConnector, SQLiteConnector, PostgreSQLConnector
from .models_api import MallCustomerModel
from typing import Optional, Union
from datetime import timedelta, datetime

def factory_connector(datastore: str):
    if 'pymysql://' in datastore:
        return MySQLConnector(datastore=datastore)
    elif 'sqlite:///' in datastore:
        return SQLiteConnector(datastore=datastore)
    elif 'postgresql://' in datastore:
        return PostgreSQLConnector(datastore=datastore)
    else:
        raise TypeError("Такой база данных не существует.")

class TableMallCustomers:
    def __init__(self, datastore: str):
        """datastore берется из .env"""
        self.Connector = factory_connector(datastore=datastore)
        self.Connector.connect()  
        
    def select_by_id(self, id: int) -> Optional[Union[tuple, str]]:
        try:
            self.Connector.start_transaction()
            result = self.Connector.execute(f"""SELECT * FROM mall_customer
                                            WHERE customerid = {id}""")
            self.Connector.end_transaction()
            return result
        except Exception as e:
            return f"Error! : {e}"
        
    def select_full_table(self) -> Optional[Union[tuple, str]]:
        try:
            self.Connector.start_transaction()
            result = self.Connector.execute(f"""SELECT * FROM mall_customer""")
            self.Connector.end_transaction()
            return result
        except Exception as e:
            return f"Error! : {e}"
    
    def delete_by_id(self, id: int) -> str:
        try:
            self.Connector.start_transaction()
            self.Connector.execute(f"""DELETE FROM mall_customer
                                   WHERE id = {id}""")
            self.Connector.end_transaction()
            return f"Deleted row by id:{id}"
        except Exception as e:
            return f"Error! : {e}"
        
    def update_by_id(self, id: int, data: dict) -> str:
        try:
            self.Connector.start_transaction()
            self.Connector.execute(f"""UPDATE mall_customer
                                   SET {data['name']} = {data['data']}
                                   WHERE customerid = {id}""")
            self.Connector.end_transaction()
            return f"Updated {data['name']} on {data['data']} row by id:{id}"
        except Exception as e:
            return f"Error! : {e}"
        

    def insert_data_in_table(self, data: MallCustomerModel) -> str:
        try:
            self.Connector.start_transaction()
            self.Connector.execute(f"""INSERT INTO mall_customer (customerid, genre, age, annual_income, spending_score)
                                   VALUES ({data.customerId}, \'{data.genre}\', {data.age}, {data.annual_income}, {data.spending_score})""")
            self.Connector.end_transaction()
            return f"Inserted data on mall_customer"
        except Exception as e:
            return f"Error! : {e}"
            

        
    
    
