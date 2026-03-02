from pydantic import BaseModel
from typing import Optional
from datetime import date

class AssignmentBase(BaseModel):
    asset_id: int
    user_id: int
    assigned_date: date

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentReturn(BaseModel):
    returned_date: date
    condition_on_return: Optional[str] = None

class AssignmentResponse(AssignmentBase):
    id: int
    returned_date: Optional[date] = None
    condition_on_return: Optional[str] = None

    class Config:
        from_attributes = True
