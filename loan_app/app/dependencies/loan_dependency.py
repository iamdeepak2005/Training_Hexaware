from app.repositories.loan_repository import LoanRepository
from app.services.loan_service import LoanService

_loan_repo = LoanRepository()
_loan_service = LoanService(loan_repo=_loan_repo)


def get_loan_service() -> LoanService:
    return _loan_service
