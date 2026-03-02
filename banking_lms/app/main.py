from fastapi import FastAPI
from .controllers import user_controller, product_controller, application_controller, repayment_controller
from .middleware.cors import add_cors_middleware
from .middleware.logging_middleware import logging_middleware
from .exceptions.exception_handlers import app_exception_handler, general_exception_handler
from .exceptions.custom_exceptions import AppException
from .core.database import Base, engine
# Create tables (For production, use Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Banking Loan Management System")

# Middlewares
add_cors_middleware(app)
app.middleware("http")(logging_middleware)

# Exception Handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Routers
app.include_router(user_controller.router)
app.include_router(product_controller.router)
app.include_router(application_controller.router)
app.include_router(repayment_controller.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Banking LMS API"}
