import os
from pony.orm import Database
from .factory import factory_database

db = Database()
info_db = factory_database(os.getenv("DB_PATH"))
db.bind(provider='postgres', 
        user=info_db['username'], 
        password=info_db['password'], 
        host=info_db['host'], 
        database=info_db['db'])