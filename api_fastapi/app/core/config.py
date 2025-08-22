import os
from pydantic_settings import BaseSettings

# Path untuk menemukan file .env di root folder proyek
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
ENV_FILE_PATH = os.path.join(ROOT_DIR, '.env')

class Settings(BaseSettings):
    # Variabel yang sudah ada
    PROJECT_NAME: str
    DATABASE_URL: str
    
    # --- TAMBAHKAN VARIABEL YANG HILANG DI SINI ---
    API_V1_STR: str
    GOOGLE_API_KEY: str
    REDIS_BROKER_URL: str
    REDIS_BACKEND_URL: str
    
    class Config:
        env_file = ENV_FILE_PATH
        env_file_encoding = 'utf-8'

settings = Settings()