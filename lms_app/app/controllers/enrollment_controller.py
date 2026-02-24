from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse, EnrollmentByStudentResponse
from app.services.enrollment_service import EnrollmentService
from app.dependencies.dependencies import get_enrollment_service

router = APIRouter(tags=["Enrollments"])


@router.post("/enrollments", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll_student(payload: EnrollmentCreate, service: EnrollmentService = Depends(get_enrollment_service)):
    try:
        return service.enroll_student(student_id=payload.student_id, course_id=payload.course_id)
    except LookupError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/enrollments", response_model=List[EnrollmentResponse])
def get_all_enrollments(service: EnrollmentService = Depends(get_enrollment_service)):
    return service.get_all_enrollments()


@router.get("/students/{student_id}/enrollments", response_model=List[EnrollmentByStudentResponse])
def get_enrollments_by_student(student_id: int, service: EnrollmentService = Depends(get_enrollment_service)):
    try:
        return service.get_enrollments_by_student(student_id)
    except LookupError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/courses/{course_id}/enrollments", response_model=List[EnrollmentResponse])
def get_enrollments_by_course(course_id: int, service: EnrollmentService = Depends(get_enrollment_service)):
    try:
        return service.get_enrollments_by_course(course_id)
    except LookupError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
