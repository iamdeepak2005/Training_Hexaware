from pydantic import BaseModel
from typing import Optional
from ..models.loan_application import LoanStatus

class ApplicationBase(BaseModel):
    product_id: int
    requested_amount: float

class ApplicationCreate(ApplicationBase):
    user_id: int

class ApplicationUpdateStatus(BaseModel):
    status: LoanStatus
    approved_amount: Optional[float] = None
    processed_by: int

class ApplicationOut(ApplicationBase):
    id: int
    user_id: int
    approved_amount: Optional[float]
    status: LoanStatus
    processed_by: Optional[int]

    class Config:
        from_attributes = True
