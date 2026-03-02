import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv()
pg_bin_path = r"C:\Program Files\PostgreSQL\18\bin" # Adjust version as needed
if os.path.exists(pg_bin_path):
    os.add_dll_directory(pg_bin_path)
class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Hiring Application API")
    
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "hiringdb")
    @property
    def DATABASE_URL(self) -> str:
        encoded_password = quote_plus(self.DB_PASSWORD)
        return f"postgresql://{self.DB_USER}:{encoded_password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
settings = Settings()
