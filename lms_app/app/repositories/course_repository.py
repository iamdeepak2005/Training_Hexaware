from typing import Dict, List, Optional


class CourseRepository:
    def __init__(self):
        self._store: Dict[int, dict] = {}
        self._counter: int = 1

    def save(self, title: str, duration: int) -> dict:
        course = {"id": self._counter, "title": title, "duration": duration}
        self._store[self._counter] = course
        self._counter += 1
        return course

    def get_by_id(self, course_id: int) -> Optional[dict]:
        return self._store.get(course_id)

    def get_all(self) -> List[dict]:
        return list(self._store.values())
