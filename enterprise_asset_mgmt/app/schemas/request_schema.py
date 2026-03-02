from pydantic import BaseModel
from typing import Optional
from enum import Enum

class RequestStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class RequestBase(BaseModel):
    asset_type: str
    reason: str

class RequestCreate(RequestBase):
    pass

class RequestUpdate(BaseModel):
    status: RequestStatus
    approved_by: Optional[int] = None

class RequestResponse(RequestBase):
    id: int
    employee_id: int
    status: RequestStatus
    approved_by: Optional[int] = None

    class Config:
        from_attributes = True
