from typing import List, Optional, Dict


class ParticipantRepository:
    def __init__(self):
        self._store: Dict[int, dict] = {}
        self._counter: int = 1

    def save(self, name: str, email: str, event_id: int) -> dict:
        participant = {
            "id": self._counter,
            "name": name,
            "email": email,
            "event_id": event_id,
        }
        self._store[self._counter] = participant
        self._counter += 1
        return participant
        
    def get_by_id(self, participant_id: int) -> Optional[dict]:
        return self._store.get(participant_id)

    def get_by_email(self, email: str) -> Optional[dict]:
        email_lower = email.strip().lower()
        for participant in self._store.values():
            if participant["email"].lower() == email_lower:
                return participant
        return None

    def get_all(self) -> List[dict]:
        return list(self._store.values())
