from .sql_connectors import PostgreSQLConnector
from .abstract_sql_connector import AbstractConnector
from .models_api import MallCustomerModel
from typing import Optional, Union

def select_by_id(connector: AbstractConnector, id: int) -> Optional[Union[tuple, str]]:
    try:
        connector.start_transaction()
        result = connector.execute(f"""SELECT * FROM mall_customer
                                        WHERE customerid = {id}""")
        if connector.__class__ == PostgreSQLConnector:
            result = connector.fetchone()
        else:
            result = result.fetchone()
        connector.end_transaction()
        return result
    except Exception as e:
        return f"Error! : {e}"
    
def select_full_table(connector: AbstractConnector) -> Optional[Union[tuple, str]]:
    try:
        connector.start_transaction()
        result = connector.execute(f"""SELECT * FROM mall_customer""")
        if connector.__class__ == PostgreSQLConnector:
            result = connector.fetchall()
        else:
            result = result.fetchall()
        connector.end_transaction()
        return result
    except Exception as e:
        return f"Error! : {e}"

def delete_by_id(connector: AbstractConnector, id: int) -> str:
    try:
        connector.start_transaction()
        connector.execute(f"""DELETE FROM mall_customer
                                WHERE customerid = {id}""")
        connector.end_transaction()
        return f"Deleted row by id:{id}"
    except Exception as e:
        return f"Error! : {e}"
    
def update_by_id(connector: AbstractConnector, id: int, data: str, data_value: Union[str, int]) -> str:
    try:
        connector.start_transaction()
        if data_value is str:
            connector.execute(f"""UPDATE mall_customer
                                SET {data} = \'{data_value}\'
                                WHERE customerid = {id}""")
        else:
            connector.execute(f"""UPDATE mall_customer
                                SET {data} = {data_value}
                                WHERE customerid = {id}""")
        connector.end_transaction()
        return f"Updated {data} on {data_value} row by id:{id}"
    except Exception as e:
        return f"Error! : {e}"
    

def insert_data_in_table(connector: AbstractConnector, data: MallCustomerModel) -> str:
    try:
        connector.start_transaction()
        connector.execute(f"""INSERT INTO mall_customer (customerid, genre, age, annual_income, spending_score)
                                VALUES ({data.customerId}, \'{data.genre}\', {data.age}, {data.annual_income}, {data.spending_score})""")
        connector.end_transaction()
        return f"Inserted data on mall_customer"
    except Exception as e:
        return f"Error! : {e}"
            

        
    
    
