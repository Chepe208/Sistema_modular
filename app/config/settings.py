import os 
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Mi App")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")

config = {
    "APP_NAME": APP_NAME,
    "APP_VERSION": APP_VERSION,
    "ADMIN_USER": ADMIN_USER,
    "ADMIN_EMAIL": ADMIN_EMAIL
}