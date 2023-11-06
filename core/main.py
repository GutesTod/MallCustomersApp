
from fastapi import FastAPI
from dotenv import load_dotenv
from backend import get_project_root_dir
from routers import info_router

load_dotenv(get_project_root_dir() / '.env')

app = FastAPI()


app.include_router(info_router)