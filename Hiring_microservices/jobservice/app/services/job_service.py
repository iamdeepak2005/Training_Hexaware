from sqlalchemy.orm import Session
from app.repositories.job_repository import JobRepository
from app.schemas.job_schema import JobCreate, JobUpdate
from typing import List

class JobService:
    def __init__(self, db: Session):
        self.repository = JobRepository(db)

    def create_job(self, job: JobCreate, owner_email: str):
        return self.repository.create_job(job, owner_email)

    def get_job(self, job_id: int):
        return self.repository.get_job(job_id)

    def get_all_jobs(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all_jobs(skip, limit)

    def update_job(self, job_id: int, job_update: JobUpdate, owner_email: str):
        return self.repository.update_job(job_id, job_update, owner_email)

    def delete_job(self, job_id: int, owner_email: str):
        return self.repository.delete_job(job_id, owner_email)
