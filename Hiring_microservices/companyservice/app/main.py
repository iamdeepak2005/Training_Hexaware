from fastapi import FastAPI
from app.database.base import Base
from app.database.session import engine
from app.routers.company_router import router as company_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(company_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Company Service"}