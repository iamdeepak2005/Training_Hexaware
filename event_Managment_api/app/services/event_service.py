from typing import List, Optional
from app.repositories.event_repository import EventRepository


class EventService:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    def create_event(self, name: str, location: str, capacity: int) -> dict:
        existing = self.event_repo.get_by_name(name)
        if existing:
            raise ValueError(f"An event named '{name}' already exists (id={existing['id']}).")

        return self.event_repo.save(name=name, location=location, capacity=capacity)

    def get_all_events(self, location: Optional[str] = None) -> List[dict]:
        if location:
            return self.event_repo.filter_by_location(location)
        return self.event_repo.get_all()

    def get_event_by_id(self, event_id: int) -> dict:
        event = self.event_repo.get_by_id(event_id)
        if not event:
            raise ValueError(f"Event with id={event_id} not found.")
        return event
