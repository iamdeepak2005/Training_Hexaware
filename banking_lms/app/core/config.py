import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv()

# Fix for psycopg2 DLL load failed on Windows if using psycopg2
pg_bin_path = r"C:\Program Files\PostgreSQL\18\bin" # Adjust version as needed
if os.path.exists(pg_bin_path):
    os.add_dll_directory(pg_bin_path)

class Settings:
    PROJECT_NAME: str = "Banking Loan Management System"
    
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "Deepak@2005")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "banking_lms")

    @property
    def DATABASE_URL(self) -> str:
        encoded_password = quote_plus(self.DB_PASSWORD)
        return f"postgresql://{self.DB_USER}:{encoded_password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
settings = Settings()
