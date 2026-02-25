from sqlalchemy.orm import Session
from ..models.repayment import Repayment
from ..schemas.repayment_schema import RepaymentCreate

class RepaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, repayment_data: RepaymentCreate):
        db_repayment = Repayment(**repayment_data.dict())
        self.db.add(db_repayment)
        self.db.commit()
        self.db.refresh(db_repayment)
        return db_repayment

    def get_by_application_id(self, app_id: int):
        return self.db.query(Repayment).filter(Repayment.loan_application_id == app_id).all()

    def get_total_paid(self, app_id: int):
        repayments = self.get_by_application_id(app_id)
        return sum(r.amount_paid for r in repayments)
