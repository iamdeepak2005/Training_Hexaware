from sqlalchemy.orm import Session
from app.models.application import Application
from app.schemas.application_schema import ApplicationCreate, ApplicationUpdate
from typing import List

class ApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_application(self, application: ApplicationCreate, user_email: str) -> Application:
        db_application = Application(**application.dict(), user_email=user_email)
        self.db.add(db_application)
        self.db.commit()
        self.db.refresh(db_application)
        return db_application

    def get_application(self, application_id: int) -> Application:
        return self.db.query(Application).filter(Application.id == application_id).first()

    def get_user_applications(self, user_email: str) -> List[Application]:
        return self.db.query(Application).filter(Application.user_email == user_email).all()

    def get_job_applications(self, job_id: int) -> List[Application]:
        return self.db.query(Application).filter(Application.job_id == job_id).all()

    def update_application_status(self, application_id: int, status: str) -> Application:
        db_application = self.get_application(application_id)
        if not db_application:
            return None
        
        db_application.status = status
        self.db.commit()
        self.db.refresh(db_application)
        return db_application

    def delete_application(self, application_id: int, user_email: str) -> bool:
        db_application = self.get_application(application_id)
        if not db_application or db_application.user_email != user_email:
            return False
        
        self.db.delete(db_application)
        self.db.commit()
        return True
