from fastapi import Request
from fastapi.responses import JSONResponse
from .custom_exceptions import HiringAppException

async def hiring_app_exception_handler(request: Request, exc: HiringAppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )
