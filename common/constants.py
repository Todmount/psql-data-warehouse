import os
from dotenv import find_dotenv, load_dotenv

from common.get_project_root import get_project_root

load_dotenv(find_dotenv())

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_SUPERUSER = os.getenv("DB_SUPERUSER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SUPERPASSWORD = os.getenv("DB_SUPERPASSWORD")

PROJECT_ROOT = get_project_root()
CRM_PATH = PROJECT_ROOT / "datasets/source_crm"
ERP_PATH = PROJECT_ROOT / "datasets/source_erp"
MODELS_PATH = PROJECT_ROOT / "models"
BRONZE_PATH = MODELS_PATH / "bronze"
SILVER_PATH = MODELS_PATH / "silver"
GOLD_PATH = MODELS_PATH / "gold"