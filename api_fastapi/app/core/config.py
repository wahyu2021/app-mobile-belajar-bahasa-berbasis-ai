from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Muat variabel dari file .env di root proyek
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env'))

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Language Game API"
    API_V1_STR: str = "/api/v1"
    GOOGLE_API_KEY: str

settings = Settings()