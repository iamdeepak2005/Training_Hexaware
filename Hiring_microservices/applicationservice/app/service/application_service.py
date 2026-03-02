from sqlalchemy.orm import Session
from app.repositories.application_repository import ApplicationRepository
from app.schemas.application_schema import ApplicationCreate, ApplicationUpdate
from typing import List

class ApplicationService:
    def __init__(self, db: Session):
        self.repository = ApplicationRepository(db)

    def apply_to_job(self, application: ApplicationCreate, user_email: str):
        return self.repository.create_application(application, user_email)

    def get_application(self, application_id: int):
        return self.repository.get_application(application_id)

    def get_my_applications(self, user_email: str):
        return self.repository.get_user_applications(user_email)

    def get_job_applications(self, job_id: int):
        return self.repository.get_job_applications(job_id)

    def update_status(self, application_id: int, status_update: ApplicationUpdate):
        return self.repository.update_application_status(application_id, status_update.status)

    def cancel_application(self, application_id: int, user_email: str):
        return self.repository.delete_application(application_id, user_email)
