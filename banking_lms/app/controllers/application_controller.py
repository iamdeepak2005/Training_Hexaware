from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..schemas.application_schema import ApplicationCreate, ApplicationUpdateStatus, ApplicationOut
from ..services.application_service import ApplicationService
from typing import List

router = APIRouter(prefix="/loan-applications", tags=["Loan Applications"])

@router.post("/", response_model=ApplicationOut)
def apply_for_loan(application: ApplicationCreate, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.apply_for_loan(application)

@router.get("/{id}", response_model=ApplicationOut)
def get_application(id: int, db: Session = Depends(get_db)):
    service = ApplicationService(id) # Wait, should be app_id in call
    service = ApplicationService(db)
    return service.get_application(id)

@router.get("/", response_model=List[ApplicationOut])
def list_applications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.list_applications(skip, limit)

@router.put("/{id}/status", response_model=ApplicationOut)
def update_status(id: int, update_data: ApplicationUpdateStatus, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.update_application_status(id, update_data)

@router.put("/{id}/disburse", response_model=ApplicationOut)
def disburse_loan(id: int, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.disburse_loan(id)
