from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.job_schema import JobCreate, JobUpdate, JobResponse
from app.services.job_service import JobService, get_job_service

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobResponse)
def create_job(job_data: JobCreate, service: JobService = Depends(get_job_service)):
    return service.create_job(job_data)

@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, service: JobService = Depends(get_job_service)):
    return service.get_job(job_id)

@router.get("/", response_model=List[JobResponse])
def list_jobs(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1), 
    service: JobService = Depends(get_job_service)
):
    return service.list_jobs(skip, limit)

@router.put("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job_data: JobUpdate, service: JobService = Depends(get_job_service)):
    return service.update_job(job_id, job_data)

@router.delete("/{job_id}")
def delete_job(job_id: int, service: JobService = Depends(get_job_service)):
    return service.delete_job(job_id)
