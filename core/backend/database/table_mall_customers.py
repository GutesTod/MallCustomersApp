from . import db
from pony.orm import *

class MallCustomerTable(db.Entity):
    _table_ = 'mall_customer'
    customerId = PrimaryKey(int, auto=False, column='customerid')
    genre = Required(str, column='genre')
    age = Required(int, column='annual_income')
    annual_income = Required(int, column='annual_income')
    spending_score = Required(int, column='spending_score')