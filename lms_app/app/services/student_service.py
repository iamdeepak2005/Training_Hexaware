from app.repositories.student_repository import StudentRepository


class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def register_student(self, name: str, email: str) -> dict:
        existing = self.student_repo.get_by_email(email)
        if existing:
            raise ValueError(f"A student with email '{email}' is already registered.")
        return self.student_repo.save(name=name, email=email)

    def get_student_by_id(self, student_id: int) -> dict:
        student = self.student_repo.get_by_id(student_id)
        if not student:
            raise ValueError(f"Student not found.")
        return student
