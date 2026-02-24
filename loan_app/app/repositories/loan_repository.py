from typing import Dict, List, Optional


class LoanRepository:
    def __init__(self):
        self._store: Dict[int, dict] = {}
        self._counter: int = 1

    def create_loan(
        self, applicant_name: str, income: float, loan_amount: float
    ) -> dict:
        loan = {
            "id": self._counter,
            "applicant_name": applicant_name,
            "income": income,
            "loan_amount": loan_amount,
            "status": "PENDING",
        }
        self._store[self._counter] = loan
        self._counter += 1
        return loan

    def get_loan_by_id(self, loan_id: int) -> Optional[dict]:
        return self._store.get(loan_id)

    def update_status(self, loan_id: int, status: str) -> Optional[dict]:
        loan = self._store.get(loan_id)
        if not loan:
            return None
        loan["status"] = status
        return loan

    def get_all_loans(self) -> List[dict]:
        return list(self._store.values())
