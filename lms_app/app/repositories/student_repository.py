from typing import Dict, List, Optional


class StudentRepository:
    def __init__(self):
        self._store: Dict[int, dict] = {}
        self._counter: int = 1

    def save(self, name: str, email: str) -> dict:
        student = {"id": self._counter, "name": name, "email": email}
        self._store[self._counter] = student
        self._counter += 1
        return student

    def get_by_id(self, student_id: int) -> Optional[dict]:
        return self._store.get(student_id)

    def get_by_email(self, email: str) -> Optional[dict]:
        email_lower = email.strip().lower()
        for student in self._store.values():
            if student["email"].lower() == email_lower:
                return student
        return None

    def get_all(self) -> List[dict]:
        return list(self._store.values())
