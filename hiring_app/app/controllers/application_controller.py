from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.application_schema import ApplicationCreate, ApplicationResponse
from app.services.application_service import ApplicationService, get_application_service

router = APIRouter(tags=["Applications"])

@router.post("/applications", response_model=ApplicationResponse)
def apply_for_job(app_data: ApplicationCreate, service: ApplicationService = Depends(get_application_service)):
    return service.apply_for_job(app_data)

@router.get("/applications/{app_id}", response_model=ApplicationResponse)
def get_application(app_id: int, service: ApplicationService = Depends(get_application_service)):
    return service.get_application(app_id)

@router.get("/users/{user_id}/applications", response_model=List[ApplicationResponse])
def get_user_applications(user_id: int, service: ApplicationService = Depends(get_application_service)):
    return service.get_user_applications(user_id)
