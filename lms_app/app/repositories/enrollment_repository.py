from typing import Dict, List


class EnrollmentRepository:
    def __init__(self):
        self._store: Dict[int, dict] = {}
        self._counter: int = 1

    def save(self, student_id: int, course_id: int) -> dict:
        enrollment = {"id": self._counter, "student_id": student_id, "course_id": course_id}
        self._store[self._counter] = enrollment
        self._counter += 1
        return enrollment

    def get_all(self) -> List[dict]:
        return list(self._store.values())

    def get_by_student(self, student_id: int) -> List[dict]:
        return [e for e in self._store.values() if e["student_id"] == student_id]

    def get_by_course(self, course_id: int) -> List[dict]:
        return [e for e in self._store.values() if e["course_id"] == course_id]

    def exists(self, student_id: int, course_id: int) -> bool:
        return any(
            e["student_id"] == student_id and e["course_id"] == course_id
            for e in self._store.values()
        )
