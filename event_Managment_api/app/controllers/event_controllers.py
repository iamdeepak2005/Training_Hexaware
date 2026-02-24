from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import List, Optional

from app.schemas.event_schema import EventCreate, EventResponse
from app.services.event_service import EventService
from app.dependencies.service_depencies import get_event_service

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.post(
    "/",
    response_model=EventResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new event",
)
def create_event(
    payload: EventCreate,
    service: EventService = Depends(get_event_service),
):

    try:
        event = service.create_event(
            name=payload.name,
            location=payload.location,
            capacity=payload.capacity,
        )
        return event
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get(
    "/",
    response_model=List[EventResponse],
    summary="List all events (optionally filter by location)",
)
def list_events(
    location: Optional[str] = Query(
        default=None,
        description="Filter events by location (partial, case-insensitive match)",
    ),
    service: EventService = Depends(get_event_service),
):

    return service.get_all_events(location=location)


@router.get(
    "/{event_id}",
    response_model=EventResponse,
    summary="Get a single event by ID",
)
def get_event(
    event_id: int,
    service: EventService = Depends(get_event_service),
):
    try:
        return service.get_event_by_id(event_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
