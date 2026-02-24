from app.repositories.participant_repository import ParticipantRepository
from app.repositories.event_repository import EventRepository


class ParticipantService:
    def __init__(
        self,
        participant_repo: ParticipantRepository,
        event_repo: EventRepository,
    ):
        self.participant_repo = participant_repo
        self.event_repo = event_repo

    def register_participant(self, name: str, email: str, event_id: int) -> dict:
        event = self.event_repo.get_by_id(event_id)
        if not event:
            raise ValueError(f"Event with id={event_id} does not exist.")

        if event["registered"] >= event["capacity"]:
            raise ValueError(
                f"Event '{event['name']}' is at full capacity "
                f"({event['capacity']} / {event['capacity']})."
            )

        existing = self.participant_repo.get_by_email(email)
        if existing:
            raise ValueError(
                f"A participant with email '{email}' is already registered "
                f"(id={existing['id']})."
            )

        participant = self.participant_repo.save(name=name, email=email, event_id=event_id)
        self.event_repo.increment_registered(event_id)
        return participant

    def get_participant_by_id(self, participant_id: int) -> dict:
        participant = self.participant_repo.get_by_id(participant_id)
        if not participant:
            raise ValueError(f"Participant with id={participant_id} not found.")
        return participant
