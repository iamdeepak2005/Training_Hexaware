from pydantic import BaseModel, Field
from typing import Optional


class EventCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Event name")
    location: str = Field(..., min_length=2, description="Event location")
    capacity: int = Field(..., gt=0, description="Maximum number of participants")


# ── Response Schema ─────────────────────────────────────────────────────────
class EventResponse(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
    registered: int

    class Config:
        from_attributes = True