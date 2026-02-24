from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse
from app.services.participant_service import ParticipantService
from app.dependencies.service_depencies import get_participant_service

router = APIRouter(
    prefix="/participants",
    tags=["Participants"],
)


# ────────────────────────────────────────────────────────────────────────────
# POST /participants  →  Register a participant for an event
# ────────────────────────────────────────────────────────────────────────────
@router.post(
    "/",
    response_model=ParticipantResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a participant for an event",
)
def register_participant(
    payload: ParticipantCreate,
    service: ParticipantService = Depends(get_participant_service),
):
    """
    Registers a participant.

    **Business rules enforced:**
    - The `event_id` must refer to an existing event
    - The event must not have reached its maximum capacity
    - The `email` must be unique (each person can only register once)
    """
    try:
        participant = service.register_participant(
            name=payload.name,
            email=payload.email,
            event_id=payload.event_id,
        )
        return participant
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# ────────────────────────────────────────────────────────────────────────────
# GET /participants/{participant_id}  →  Fetch participant details
# ────────────────────────────────────────────────────────────────────────────
@router.get(
    "/{participant_id}",
    response_model=ParticipantResponse,
    summary="Get participant details by ID",
)
def get_participant(
    participant_id: int,
    service: ParticipantService = Depends(get_participant_service),
):
    """
    Returns the details of a registered participant.  
    Returns **404** if no participant with the given id exists.
    """
    try:
        return service.get_participant_by_id(participant_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
