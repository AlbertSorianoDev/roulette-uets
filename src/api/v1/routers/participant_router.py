from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Optional
from sqlalchemy.orm import Session

from src.core.config.database import get_session
from src.core.schemas.participant_schema import (
    ParticipantSchema,
    ParticipantCreateSchema,
)
from src.api.v1.services.participant_service import ParticipantService

participant_router = APIRouter(prefix="/participants", tags=["Participants"])


@participant_router.get("/", response_model=List[ParticipantSchema])
async def get_participants(db_session: Session = Depends(get_session)):
    service = ParticipantService(db_session)
    result = service.get_participants()

    return JSONResponse(content=result, status_code=200)


@participant_router.post("/", response_model=Optional[ParticipantSchema])
async def add_participant(
    participant: ParticipantCreateSchema,
    db_session: Session = Depends(get_session),
):
    service = ParticipantService(db_session)
    result = service.add_participant(participant)

    if result:
        return JSONResponse(content=result.model_to_dict(), status_code=201)
    else:
        return JSONResponse(content=None, status_code=400)
