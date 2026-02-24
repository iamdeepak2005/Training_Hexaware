from typing import List
from app.repositories.loan_repository import LoanRepository


class LoanService:
    def __init__(self, loan_repo: LoanRepository):
        self.loan_repo = loan_repo

    def submit_application(
        self, applicant_name: str, income: float, loan_amount: float
    ) -> dict:
        if income <= 0:
            raise ValueError("Income must be greater than zero.")

        eligibility_limit = income * 10
        if loan_amount > eligibility_limit:
            raise ValueError(
                f"Loan amount exceeds eligibility limit of {eligibility_limit}."
            )

        return self.loan_repo.create_loan(
            applicant_name=applicant_name,
            income=income,
            loan_amount=loan_amount,
        )

    def get_application(self, loan_id: int) -> dict:
        loan = self.loan_repo.get_loan_by_id(loan_id)
        if not loan:
            raise ValueError(f"Loan application not found")
        return loan

    def approve_loan(self, loan_id: int) -> dict:
        loan = self.loan_repo.get_loan_by_id(loan_id)
        if not loan:
            raise ValueError("Loan application not found")

        if loan["status"] != "PENDING":
            raise ValueError("Only pending loans can be approved")

        eligibility_limit = loan["income"] * 10
        if loan["loan_amount"] > eligibility_limit:
            raise ValueError("Loan amount exceeds eligibility limit")

        return self.loan_repo.update_status(loan_id, "APPROVED")

    def reject_loan(self, loan_id: int) -> dict:
        loan = self.loan_repo.get_loan_by_id(loan_id)
        if not loan:
            raise ValueError("Loan application not found")

        if loan["status"] != "PENDING":
            raise ValueError("Only pending loans can be rejected")

        return self.loan_repo.update_status(loan_id, "REJECTED")

    def list_all_applications(self) -> List[dict]:
        return self.loan_repo.get_all_loans()
