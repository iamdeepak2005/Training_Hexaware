from fastapi import FastAPI
from app.database.base import Base
from app.database.session import engine
from app.routers import job_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Service")

app.include_router(job_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Service"}
