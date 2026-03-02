from fastapi  import FastAPI
from app.routers import auth_router
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Auth")

app.include_router(auth_router.router)

@app.get("/")
def read_root():
    return {"message":"Welcome to the Authentication Service"}