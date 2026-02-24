from fastapi import FastAPI
from app.controllers.loan_controller import router as loan_router
from app.middleware.cors import add_cors_middleware
from app.core.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Loan Application and Approval Management System",
)

add_cors_middleware(app)

app.include_router(loan_router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "running", "app": APP_NAME, "version": APP_VERSION}
