from pydantic import BaseModel
from typing import Optional, List

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    manager_id: Optional[int] = None

class DepartmentResponse(DepartmentBase):
    id: int
    manager_id: Optional[int] = None

    class Config:
        from_attributes = True
