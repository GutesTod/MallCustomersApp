from fastapi import APIRouter

info_router = APIRouter()

@info_router.get("/info/get_mail_customers")
async def get_mail_customers():
    ...