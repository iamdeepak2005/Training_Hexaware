from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.schemas.application_schema import ApplicationCreate, ApplicationUpdate, ApplicationResponse
from app.service.application_service import ApplicationService
from app.core.security import get_current_user

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
def apply(application: ApplicationCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = ApplicationService(db)
    return service.apply_to_job(application, current_user)

@router.get("/me", response_model=List[ApplicationResponse])
def read_my_applications(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = ApplicationService(db)
    return service.get_my_applications(current_user)

@router.get("/job/{job_id}", response_model=List[ApplicationResponse])
def read_job_applications(job_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    # In a real app, we'd check if current_user is the owner of the job
    service = ApplicationService(db)
    return service.get_job_applications(job_id)

@router.get("/{application_id}", response_model=ApplicationResponse)
def read_application(application_id: int, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    app_record = service.get_application(application_id)
    if not app_record:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_record

@router.put("/{application_id}/status", response_model=ApplicationResponse)
def update_application_status(application_id: int, status_update: ApplicationUpdate, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    updated_app = service.update_status(application_id, status_update)
    if not updated_app:
        raise HTTPException(status_code=404, detail="Application not found")
    return updated_app

@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_application(application_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = ApplicationService(db)
    if not service.cancel_application(application_id, current_user):
        raise HTTPException(status_code=404, detail="Application not found or not authorized")
    return None
