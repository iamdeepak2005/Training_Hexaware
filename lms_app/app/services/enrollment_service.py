from typing import List
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository


class EnrollmentService:
    def __init__(self, enrollment_repo: EnrollmentRepository, student_repo: StudentRepository, course_repo: CourseRepository):
        self.enrollment_repo = enrollment_repo
        self.student_repo = student_repo
        self.course_repo = course_repo

    def enroll_student(self, student_id: int, course_id: int) -> dict:
        student = self.student_repo.get_by_id(student_id)
        if not student:
            raise LookupError("Student not found.")

        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise LookupError("Course not found.")

        if self.enrollment_repo.exists(student_id=student_id, course_id=course_id):
            raise ValueError("Already enrolled.")

        return self.enrollment_repo.save(student_id=student_id, course_id=course_id)

    def get_all_enrollments(self) -> List[dict]:
        return self.enrollment_repo.get_all()

    def get_enrollments_by_student(self, student_id: int) -> List[dict]:
        student = self.student_repo.get_by_id(student_id)
        if not student:
            raise LookupError("Student not found.")

        enrollments = self.enrollment_repo.get_by_student(student_id)
        result = []
        for e in enrollments:
            course = self.course_repo.get_by_id(e["course_id"])
            result.append({
                "course_id": e["course_id"],
                "course_title": course["title"] if course else "Unknown",
            })
        return result

    def get_enrollments_by_course(self, course_id: int) -> List[dict]:
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise LookupError("Course not found.")
        return self.enrollment_repo.get_by_course(course_id)
