from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job_schema import JobCreate, JobUpdate
from typing import List

class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_job(self, job: JobCreate, owner_email: str) -> Job:
        db_job = Job(**job.dict(), owner_email=owner_email)
        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)
        return db_job

    def get_job(self, job_id: int) -> Job:
        return self.db.query(Job).filter(Job.id == job_id).first()

    def get_all_jobs(self, skip: int = 0, limit: int = 100) -> List[Job]:
        return self.db.query(Job).offset(skip).limit(limit).all()

    def get_jobs_by_company(self, company_id: int) -> List[Job]:
        return self.db.query(Job).filter(Job.company_id == company_id).all()

    def update_job(self, job_id: int, job_update: JobUpdate, owner_email: str) -> Job:
        db_job = self.get_job(job_id)
        if not db_job or db_job.owner_email != owner_email:
            return None
        
        update_data = job_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_job, key, value)
        
        self.db.commit()
        self.db.refresh(db_job)
        return db_job

    def delete_job(self, job_id: int, owner_email: str) -> bool:
        db_job = self.get_job(job_id)
        if not db_job or db_job.owner_email != owner_email:
            return False
        
        self.db.delete(db_job)
        self.db.commit()
        return True
