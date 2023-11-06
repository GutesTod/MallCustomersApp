from fastapi import APIRouter
from backend.database import MallCustomerModel


info_router = APIRouter()

@info_router.get("/info/get_mail_customers/{customerId}")
async def get_mail_customers(customerId: int) -> dict:
    