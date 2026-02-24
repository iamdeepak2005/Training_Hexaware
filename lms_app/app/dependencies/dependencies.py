from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService

_student_repo = StudentRepository()
_course_repo = CourseRepository()
_enrollment_repo = EnrollmentRepository()

_student_service = StudentService(student_repo=_student_repo)
_course_service = CourseService(course_repo=_course_repo)
_enrollment_service = EnrollmentService(
    enrollment_repo=_enrollment_repo,
    student_repo=_student_repo,
    course_repo=_course_repo,
)


def get_student_service() -> StudentService:
    return _student_service


def get_course_service() -> CourseService:
    return _course_service


def get_enrollment_service() -> EnrollmentService:
    return _enrollment_service
