from typing import Optional


class LoanApplication:
    def __init__(
        self,
        id: int,
        applicant_name: str,
        income: float,
        loan_amount: float,
        status: str = "PENDING",
    ):
        self.id = id
        self.applicant_name = applicant_name
        self.income = income
        self.loan_amount = loan_amount
        self.status = status
