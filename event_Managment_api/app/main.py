from fastapi import FastAPI
from app.controllers import event_controllers, participant_controller
from app.middleware.cors_middleware import add_cors_middleware
from app.core.db import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Event Management System API",
)

# Middleware
add_cors_middleware(app)

# Routers
app.include_router(event_controllers.router)
app.include_router(participant_controller.router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "running", "app": APP_NAME, "version": APP_VERSION}
