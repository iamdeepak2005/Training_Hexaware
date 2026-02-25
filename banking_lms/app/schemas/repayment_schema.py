from pydantic import BaseModel
from datetime import datetime
from ..models.repayment import PaymentStatus

class RepaymentBase(BaseModel):
    loan_application_id: int
    amount_paid: float

class RepaymentCreate(RepaymentBase):
    pass

class RepaymentOut(RepaymentBase):
    id: int
    payment_date: datetime
    payment_status: PaymentStatus

    class Config:
        from_attributes = True
