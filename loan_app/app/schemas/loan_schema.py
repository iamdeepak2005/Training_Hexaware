from pydantic import BaseModel, Field
from typing import Optional


class LoanCreate(BaseModel):
    applicant_name: str = Field(..., min_length=2)
    income: float = Field(..., gt=0)
    loan_amount: float = Field(..., gt=0)


class LoanResponse(BaseModel):
    id: int
    applicant_name: str
    income: float
    loan_amount: float
    status: str


class LoanSummary(BaseModel):
    id: int
    applicant_name: str
    loan_amount: float
    status: str


class LoanStatusUpdate(BaseModel):
    message: str
    status: str
