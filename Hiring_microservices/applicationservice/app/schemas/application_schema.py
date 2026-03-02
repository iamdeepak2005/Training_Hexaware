from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ApplicationBase(BaseModel):
    job_id: int
    resume_url: str
    cover_letter: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    status: Optional[str] = None # For HR to update

class ApplicationResponse(ApplicationBase):
    id: int
    user_email: str
    status: str
    applied_at: datetime

    class Config:
        from_attributes = True
