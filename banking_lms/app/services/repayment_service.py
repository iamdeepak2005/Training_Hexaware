from sqlalchemy.orm import Session
from ..repositories.repayment_repository import RepaymentRepository
from ..repositories.application_repository import ApplicationRepository
from ..schemas.repayment_schema import RepaymentCreate
from ..models.loan_application import LoanStatus
from fastapi import HTTPException

class RepaymentService:
    def __init__(self, db: Session):
        self.repository = RepaymentRepository(db)
        self.app_repo = ApplicationRepository(db)

    def add_repayment(self, repayment_data: RepaymentCreate):
        app = self.app_repo.get_by_id(repayment_data.loan_application_id)
        if not app:
            raise HTTPException(status_code=404, detail="Loan application not found")
        
        if app.status != LoanStatus.DISBURSED:
            raise HTTPException(status_code=400, detail="Loan must be disbursed before repayment")

        repayment = self.repository.create(repayment_data)
        
        # Check if loan is fully repaid
        total_paid = self.repository.get_total_paid(app.id)
        if total_paid >= app.approved_amount:
            self.app_repo.update_status(app.id, LoanStatus.CLOSED)
            
        return repayment

    def get_repayments_by_app(self, app_id: int):
        return self.repository.get_by_application_id(app_id)
