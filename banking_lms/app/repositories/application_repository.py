from sqlalchemy.orm import Session
from ..models.loan_application import LoanApplication, LoanStatus
from ..schemas.application_schema import ApplicationCreate

class ApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, app_id: int):
        return self.db.query(LoanApplication).filter(LoanApplication.id == app_id).first()

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(LoanApplication).offset(skip).limit(limit).all()

    def create(self, app_data: ApplicationCreate):
        db_app = LoanApplication(**app_data.dict())
        self.db.add(db_app)
        self.db.commit()
        self.db.refresh(db_app)
        return db_app

    def update_status(self, app_id: int, status: LoanStatus, approved_amount: float = None, processed_by: int = None):
        db_app = self.get_by_id(app_id)
        if db_app:
            db_app.status = status
            if approved_amount is not None:
                db_app.approved_amount = approved_amount
            if processed_by is not None:
                db_app.processed_by = processed_by
            self.db.commit()
            self.db.refresh(db_app)
        return db_app
