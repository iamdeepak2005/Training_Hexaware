from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.schemas.job_schema import JobCreate, JobUpdate, JobResponse
from app.services.job_service import JobService
from app.core.security import get_current_user

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = JobService(db)
    return service.create_job(job, current_user)

@router.get("/", response_model=List[JobResponse])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = JobService(db)
    return service.get_all_jobs(skip=skip, limit=limit)

@router.get("/{job_id}", response_model=JobResponse)
def read_job(job_id: int, db: Session = Depends(get_db)):
    service = JobService(db)
    job = service.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.put("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job_update: JobUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = JobService(db)
    updated_job = service.update_job(job_id, job_update, current_user)
    if not updated_job:
        raise HTTPException(status_code=404, detail="Job not found or not authorized")
    return updated_job

@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = JobService(db)
    if not service.delete_job(job_id, current_user):
        raise HTTPException(status_code=404, detail="Job not found or not authorized")
    return None
