from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.course_schema import CourseCreate, CourseResponse
from app.services.course_service import CourseService
from app.dependencies.dependencies import get_course_service

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(payload: CourseCreate, service: CourseService = Depends(get_course_service)):
    return service.create_course(title=payload.title, duration=payload.duration)


@router.get("/", response_model=List[CourseResponse])
def list_courses(service: CourseService = Depends(get_course_service)):
    return service.get_all_courses()


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, service: CourseService = Depends(get_course_service)):
    try:
        return service.get_course_by_id(course_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
