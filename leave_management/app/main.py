from fastapi import FastAPI
from app.core.config import settings
from app.database import base
from app.models.user import User
from app.models.department import Department
from app.models.leave_request import LeaveRequest
from app.database.session import engine
from app.routers import auth_router, admin_router, manager_router, employee_router
from app.middleware.logging import LoggingMiddleware
from app.middleware.exception_handler import global_exception_handler

# Create database tables
base.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# Middleware
app.add_middleware(LoggingMiddleware)
app.add_exception_handler(Exception, global_exception_handler)

# Routers
app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(manager_router.router)
app.include_router(employee_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to Enterprise Leave Management System (ELMS)"}
