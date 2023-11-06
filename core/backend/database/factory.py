import os
from dotenv import load_dotenv
from pony.orm import *
from backend import get_project_root_dir

load_dotenv(get_project_root_dir() / '.env')

def factory_database(url_db: str) -> dict:
    info_db = {}
    if 'postgresql://' in url_db:
        url_db = url_db[13:]
        info_db['provider'] = 'postgres'
        con_str_list = url_db.split(':')
        info_db['username'] = con_str_list[0]
        con_str_list = con_str_list[1].split('@')
        info_db['password'] = con_str_list[0]
        con_str_list = con_str_list[1].split('/')
        info_db['host'] = con_str_list[0]
        info_db['db'] = con_str_list[1]
    else:
        raise ValueError("In .env incorrect url DB")
    return info_db
        
        
db = Database()
info_db = factory_database(os.getenv("DB_PATH"))
db.bind(provider='postgres', 
        user=info_db['username'], 
        password=info_db['password'], 
        host=info_db['host'], 
        database=info_db['db'])
db.generate_mapping()