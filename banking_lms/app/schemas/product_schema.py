from pydantic import BaseModel
from typing import Optional

class LoanProductBase(BaseModel):
    product_name: str
    interest_rate: float
    max_amount: float
    tenure_months: int
    description: Optional[str] = None

class LoanProductCreate(LoanProductBase):
    pass

class LoanProductUpdate(BaseModel):
    product_name: Optional[str] = None
    interest_rate: Optional[float] = None
    max_amount: Optional[float] = None
    tenure_months: Optional[int] = None
    description: Optional[str] = None

class LoanProductOut(LoanProductBase):
    id: int

    class Config:
        from_attributes = True
