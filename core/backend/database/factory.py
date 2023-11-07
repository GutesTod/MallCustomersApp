import os
from .sql_connectors import MySQLConnector, SQLiteConnector, PostgreSQLConnector
from dotenv import load_dotenv
from backend import get_project_root_dir

load_dotenv(get_project_root_dir() / '.env')

def factory_connector():
    if 'pymysql://' in os.getenv('DB_PATH'):
        return MySQLConnector(datastore=os.getenv('DB_PATH'))
    elif 'sqlite:///' in os.getenv('DB_PATH'):
        return SQLiteConnector(datastore=os.getenv('DB_PATH'))
    elif 'postgresql://' in os.getenv('DB_PATH'):
        return PostgreSQLConnector(datastore=os.getenv('DB_PATH'))
    else:
        raise TypeError("Такой база данных не существует.") 
