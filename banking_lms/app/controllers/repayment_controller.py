from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..schemas.repayment_schema import RepaymentCreate, RepaymentOut
from ..services.repayment_service import RepaymentService
from typing import List

router = APIRouter(tags=["Repayments"])

@router.post("/repayments", response_model=RepaymentOut)
def add_repayment(repayment: RepaymentCreate, db: Session = Depends(get_db)):
    service = RepaymentService(db)
    return service.add_repayment(repayment)

@router.get("/loan-applications/{id}/repayments", response_model=List[RepaymentOut])
def get_repayments(id: int, db: Session = Depends(get_db)):
    service = RepaymentService(db)
    return service.get_repayments_by_app(id)
