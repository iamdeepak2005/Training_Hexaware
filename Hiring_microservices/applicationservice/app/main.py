from fastapi import FastAPI
from app.database.base import Base
from app.database.session import engine
from app.routers import application_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Application Service")

app.include_router(application_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Application Service"}
