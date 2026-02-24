from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(...)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
