from typing import List, Optional, Dict


class EventRepository:
    def __init__(self):
        self._store: Dict[int, dict] = {}
        self._counter: int = 1

    def save(self, name: str, location: str, capacity: int) -> dict:
        event = {
            "id": self._counter,
            "name": name,
            "location": location,
            "capacity": capacity,
            "registered": 0,
        }
        self._store[self._counter] = event
        self._counter += 1
        return event

    def increment_registered(self, event_id: int) -> None:
        if event_id in self._store:
            self._store[event_id]["registered"] += 1

    def get_all(self) -> List[dict]:
        return list(self._store.values())

    def get_by_id(self, event_id: int) -> Optional[dict]:
        return self._store.get(event_id)

    def get_by_name(self, name: str) -> Optional[dict]:
        name_lower = name.strip().lower()
        for event in self._store.values():
            if event["name"].lower() == name_lower:
                return event
        return None

    def filter_by_location(self, location: str) -> List[dict]:
        location_lower = location.strip().lower()
        return [
            event for event in self._store.values()
            if location_lower in event["location"].lower()
        ]
