from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job_schema import JobCreate, JobUpdate

class JobRepository:
    @staticmethod
    def get_by_id(db: Session, job_id: int):
        return db.query(Job).filter(Job.id == job_id).first()

    @staticmethod
    def list(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Job).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, job_data: JobCreate):
        db_job = Job(**job_data.dict())
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job

    @staticmethod
    def update(db: Session, db_job: Job, job_data: JobUpdate):
        data = job_data.dict(exclude_unset=True)
        for key, value in data.items():
            setattr(db_job, key, value)
        db.commit()
        db.refresh(db_job)
        return db_job

    @staticmethod
    def delete(db: Session, db_job: Job):
        db.delete(db_job)
        db.commit()
