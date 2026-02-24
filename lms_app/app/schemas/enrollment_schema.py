from pydantic import BaseModel, Field


class EnrollmentCreate(BaseModel):
    student_id: int = Field(..., gt=0)
    course_id: int = Field(..., gt=0)


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int

    class Config:
        from_attributes = True


class EnrollmentByStudentResponse(BaseModel):
    course_id: int
    course_title: str

    class Config:
        from_attributes = True
