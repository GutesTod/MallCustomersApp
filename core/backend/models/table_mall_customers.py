from backend.models import db
from pony.orm import *

class MallCustomer(db.Entity):
    __table_name__ = 'mall_customer'
    customerId = PrimaryKey(int, auto=False)
    genre = Required(str)
    age = Required(int)
    annual_income = Required(int)
    spending_score = Required(int)