from sqlalchemy.orm import Session
from app.models.application import Application
from app.schemas.application_schema import ApplicationCreate

class ApplicationRepository:
    @staticmethod
    def get_by_id(db: Session, application_id: int):
        return db.query(Application).filter(Application.id == application_id).first()

    @staticmethod
    def get_by_user_id(db: Session, user_id: int):
        return db.query(Application).filter(Application.user_id == user_id).all()

    @staticmethod
    def list(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Application).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, app_data: ApplicationCreate):
        db_app = Application(**app_data.dict())
        db.add(db_app)
        db.commit()
        db.refresh(db_app)
        return db_app

    @staticmethod
    def delete(db: Session, db_app: Application):
        db.delete(db_app)
        db.commit()
