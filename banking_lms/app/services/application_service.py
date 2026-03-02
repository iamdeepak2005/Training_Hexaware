from sqlalchemy.orm import Session
from ..repositories.application_repository import ApplicationRepository
from ..repositories.product_repository import ProductRepository
from ..repositories.user_repository import UserRepository
from ..schemas.application_schema import ApplicationCreate, ApplicationUpdateStatus
from ..models.loan_application import LoanStatus
from ..models.user import UserRole
from fastapi import HTTPException

class ApplicationService:
    def __init__(self, db: Session):
        self.repository = ApplicationRepository(db)
        self.product_repo = ProductRepository(db)
        self.user_repo = UserRepository(db)

    def apply_for_loan(self, app_data: ApplicationCreate):
        product = self.product_repo.get_by_id(app_data.product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Loan product not found")
        
        if app_data.requested_amount > product.max_amount:
            raise HTTPException(status_code=400, detail=f"Requested amount exceeds product max limit of {product.max_amount}")
        
        return self.repository.create(app_data)

    def update_application_status(self, app_id: int, update_data: ApplicationUpdateStatus):
        app = self.repository.get_by_id(app_id)
        if not app:
            raise HTTPException(status_code=404, detail="Application not found")

        officer = self.user_repo.get_by_id(update_data.processed_by)
        if not officer or officer.role != UserRole.LOAN_OFFICER:
            raise HTTPException(status_code=403, detail="Only loan officers can process applications")

        return self.repository.update_status(
            app_id, 
            update_data.status, 
            update_data.approved_amount, 
            update_data.processed_by
        )

    def disburse_loan(self, app_id: int):
        app = self.repository.get_by_id(app_id)
        if not app:
            raise HTTPException(status_code=404, detail="Application not found")
        
        if app.status != LoanStatus.APPROVED:
            raise HTTPException(status_code=400, detail="Only approved loans can be disbursed")
        
        return self.repository.update_status(app_id, LoanStatus.DISBURSED)

    def get_application(self, app_id: int):
        app = self.repository.get_by_id(app_id)
        if not app:
            raise HTTPException(status_code=404, detail="Application not found")
        return app

    def list_applications(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
