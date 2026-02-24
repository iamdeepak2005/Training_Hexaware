from fastapi import FastAPI
from app.core.db import APP_NAME, APP_VERSION
from app.middleware.cors import add_cors_middleware
from app.controllers import student_controller, course_controller, enrollment_controller

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Learning Management System API",
)

add_cors_middleware(app)

app.include_router(student_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "running", "app": APP_NAME, "version": APP_VERSION}
