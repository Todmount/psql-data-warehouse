import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_SUPERUSER = os.getenv("DB_SUPERUSER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SUPERPASSWORD = os.getenv("DB_SUPERPASSWORD")
