from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.student_schema import StudentCreate, StudentResponse
from app.services.student_service import StudentService
from app.dependencies.dependencies import get_student_service

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def register_student(payload: StudentCreate, service: StudentService = Depends(get_student_service)):
    try:
        return service.register_student(name=payload.name, email=payload.email)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, service: StudentService = Depends(get_student_service)):
    try:
        return service.get_student_by_id(student_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
