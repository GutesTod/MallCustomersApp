from pydantic import BaseModel

class MallCustomerModel(BaseModel):
    customerId: int
    genre: str
    age: int
    annual_income: int
    spending_score: int
    