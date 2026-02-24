from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.schemas.loan_schema import LoanCreate, LoanResponse, LoanSummary, LoanStatusUpdate
from app.services.loan_service import LoanService
from app.dependencies.loan_dependency import get_loan_service

router = APIRouter(prefix="/loans", tags=["Loans"])


@router.post("/", response_model=LoanResponse, status_code=status.HTTP_201_CREATED)
def submit_loan(payload: LoanCreate, service: LoanService = Depends(get_loan_service)):
    try:
        return service.submit_application(
            applicant_name=payload.applicant_name,
            income=payload.income,
            loan_amount=payload.loan_amount,
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[LoanSummary])
def get_all_loans(service: LoanService = Depends(get_loan_service)):
    return service.list_all_applications()


@router.get("/{loan_id}", response_model=LoanResponse)
def get_loan(loan_id: int, service: LoanService = Depends(get_loan_service)):
    try:
        return service.get_application(loan_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{loan_id}/approve", response_model=LoanStatusUpdate)
def approve_loan(loan_id: int, service: LoanService = Depends(get_loan_service)):
    try:
        loan = service.approve_loan(loan_id)
        return {"message": "Loan approved successfully", "status": loan["status"]}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{loan_id}/reject", response_model=LoanStatusUpdate)
def reject_loan(loan_id: int, service: LoanService = Depends(get_loan_service)):
    try:
        loan = service.reject_loan(loan_id)
        return {"message": "Loan rejected", "status": loan["status"]}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
