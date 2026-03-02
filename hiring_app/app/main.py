from fastapi import FastAPI
from app.core.database import engine
from app.models.base import Base
# Import models to ensure they are registered with Base
from app.models.user import User
from app.models.job import Job
from app.models.application import Application
from app.controllers import user_controller, job_controller, application_controller
from app.exceptions.custom_exceptions import HiringAppException
from app.exceptions.exception_handlers import hiring_app_exception_handler
from app.middleware.cors import add_cors_middleware
from app.middleware.logging import logging_middleware

# Create tables
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Hiring Application")

# Middleware
add_cors_middleware(app)
app.middleware("http")(logging_middleware)

# Exception Handlers
app.add_exception_handler(HiringAppException, hiring_app_exception_handler)

# Routers
app.include_router(user_controller.router)
app.include_router(job_controller.router)
app.include_router(application_controller.router)

@app.get("/")
def health_check():
    return {"status": "online", "message": "Hiring API is running"}
