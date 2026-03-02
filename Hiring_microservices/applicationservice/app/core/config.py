import os 
from dotenv import load_dotenv

load_dotenv()

pg_bin_path = r"C:\Program Files\PostgreSQL\18\bin"
if os.path.exists(pg_bin_path) and hasattr(os, "add_dll_directory"):
    os.add_dll_directory(pg_bin_path)

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

settings = Settings()
