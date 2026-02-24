from pydantic import BaseModel, EmailStr, Field

class ParticipantCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Participant full name")
    email: EmailStr = Field(..., description="Participant email (must be unique)")
    event_id: int = Field(..., gt=0, description="ID of the event to register for")

class ParticipantResponse(BaseModel):
    id: int
    name: str
    email: str
    event_id: int

    class Config:
        from_attributes = True