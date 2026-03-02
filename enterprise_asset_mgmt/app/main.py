from fastapi import FastAPI, Request
from app.database.base import Base
from app.database.session import engine
from app.middleware.logging import logging_middleware
from app.middleware.exception_handler import global_exception_handler

# Ensure all models are imported before create_all
# Important to import them in an order or just all together so they register with Base.metadata
from app.models.department import Department # noqa
from app.models.user import User # noqa
from app.models.asset import Asset # noqa
from app.models.asset_assignment import AssetAssignment # noqa
from app.models.asset_request import AssetRequest # noqa

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Enterprise Asset Management System")

# Routers
from app.routers import auth_router, superadmin_router, itadmin_router, manager_router, employee_router

# Middleware
@app.middleware("http")
async def add_logging_middleware(request: Request, call_next):
    return await logging_middleware(request, call_next)

app.add_exception_handler(Exception, global_exception_handler)

# include routers
app.include_router(auth_router.router)
app.include_router(superadmin_router.router)
app.include_router(itadmin_router.router)
app.include_router(manager_router.router)
app.include_router(employee_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Enterprise Asset Management System API"}
