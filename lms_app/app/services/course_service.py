from app.repositories.course_repository import CourseRepository


class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def create_course(self, title: str, duration: int) -> dict:
        return self.course_repo.save(title=title, duration=duration)

    def get_course_by_id(self, course_id: int) -> dict:
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise ValueError(f"Course not found.")
        return course

    def get_all_courses(self) -> list:
        return self.course_repo.get_all()
