from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class JobBase(BaseModel):
    title: str
    description: str
    company_id: int
    location: Optional[str] = None
    salary: Optional[str] = None
    job_type: Optional[str] = "full-time"

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    company_id: Optional[int] = None
    location: Optional[str] = None
    salary: Optional[str] = None
    job_type: Optional[str] = None

class JobResponse(JobBase):
    id: int
    owner_email: str
    created_at: datetime

    class Config:
        from_attributes = True
        # For Pydantic v1 compatibility if needed:
        # orm_mode = True
