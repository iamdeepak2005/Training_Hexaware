from pydantic import BaseModel
from typing import Optional

class ApplicationBase(BaseModel):
    user_id: int
    job_id: int
    status: Optional[str] = "applied"

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: int

    class Config:
        from_attributes = True
