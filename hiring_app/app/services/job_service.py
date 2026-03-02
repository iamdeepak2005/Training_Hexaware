from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.job_repository import JobRepository
from app.schemas.job_schema import JobCreate, JobUpdate
from app.exceptions.custom_exceptions import JobNotFoundException

class JobService:
    def __init__(self, db: Session):
        self.db = db

    def get_job(self, job_id: int):
        job = JobRepository.get_by_id(self.db, job_id)
        if not job:
            raise JobNotFoundException()
        return job

    def list_jobs(self, skip: int = 0, limit: int = 100):
        return JobRepository.list(self.db, skip, limit)

    def create_job(self, job_data: JobCreate):
        return JobRepository.create(self.db, job_data)

    def update_job(self, job_id: int, job_data: JobUpdate):
        db_job = self.get_job(job_id)
        return JobRepository.update(self.db, db_job, job_data)

    def delete_job(self, job_id: int):
        db_job = self.get_job(job_id)
        JobRepository.delete(self.db, db_job)
        return {"message": "Job deleted successfully"}

def get_job_service(db: Session = Depends(get_db)):
    return JobService(db)
