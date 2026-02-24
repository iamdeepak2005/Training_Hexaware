from pydantic import BaseModel, Field


class CourseCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=150)
    duration: int = Field(..., gt=0)


class CourseResponse(BaseModel):
    id: int
    title: str
    duration: int

    class Config:
        from_attributes = True
