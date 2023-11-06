from fastapi import APIRouter
from backend.database import MallCustomerModel, MallCustomerTable
from pony.orm import *


info_router = APIRouter()

@info_router.get("/info/get_mail_customers/{customerId}")
async def get_mail_customers(customerId: int) -> dict:
    with db_session:
        customer = MallCustomerTable[customerId]
        result = MallCustomerModel.from_orm(customerId)