
from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository
from app.services.event_service import EventService
from app.services.participant_service import ParticipantService

_event_repo = EventRepository()
_participant_repo = ParticipantRepository()

_event_service = EventService(event_repo=_event_repo)
_participant_service = ParticipantService(
    participant_repo=_participant_repo,
    event_repo=_event_repo,
)

def get_event_service() -> EventService:
    return _event_service

def get_participant_service() -> ParticipantService:
    return _participant_service
