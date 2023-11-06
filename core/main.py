from fastapi import FastAPI
from dotenv import load_dotenv
from backend import get_project_root_dir

load_dotenv(get_project_root_dir() / '.env')