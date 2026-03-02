from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.application_repository import ApplicationRepository
from app.repositories.user_repository import UserRepository
from app.repositories.job_repository import JobRepository
from app.schemas.application_schema import ApplicationCreate
from app.exceptions.custom_exceptions import (
    ApplicationNotFoundException, 
    UserNotFoundException, 
    JobNotFoundException
)

class ApplicationService:
    def __init__(self, db: Session):
        self.db = db

    def apply_for_job(self, app_data: ApplicationCreate):
        if not UserRepository.get_by_id(self.db, app_data.user_id):
            raise UserNotFoundException()
        
        if not JobRepository.get_by_id(self.db, app_data.job_id):
            raise JobNotFoundException()
            
        return ApplicationRepository.create(self.db, app_data)

    def get_application(self, app_id: int):
        app = ApplicationRepository.get_by_id(self.db, app_id)
        if not app:
            raise ApplicationNotFoundException()
        return app

    def get_user_applications(self, user_id: int):
        if not UserRepository.get_by_id(self.db, user_id):
            raise UserNotFoundException()
        return ApplicationRepository.get_by_user_id(self.db, user_id)

def get_application_service(db: Session = Depends(get_db)):
    return ApplicationService(db)
