from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from typing import List, Optional
from sqlalchemy.orm import Session
from uuid import UUID

from src.core.config.database import get_session
from src.core.schemas.record_schema import RecordSchema
from src.api.v1.services.record_service import RecordService

record_router = APIRouter(prefix="/records", tags=["Records"])


@record_router.get("/game/{game_id}", response_model=List[RecordSchema])
async def get_records_by_game_id(
    game_id: UUID,
    db_session: Session = Depends(get_session),
):
    service = RecordService(db_session)
    result = service.get_records_by_game_id(game_id)

    return JSONResponse(content=result, status_code=200)


@record_router.get("/participant_game", response_model=Optional[RecordSchema])
async def get_record_by_game_id_and_participant_id(
    game_id: UUID,
    participant_id: UUID,
    db_session: Session = Depends(get_session),
):
    service = RecordService(db_session)
    result = service.get_record_by_game_id_and_participant_id(game_id, participant_id)

    return JSONResponse(content=result, status_code=200)


@record_router.put(
    "/add_challenge_point",
    response_model=Optional[RecordSchema],
)
async def add_challenge_point(
    record_id: UUID,
    amount: int = Query(
        ...,
        ge=1,
        description="The amount to add, must be an integer greater than or equal to 1",
    ),
    db_session: Session = Depends(get_session),
):
    service = RecordService(db_session)
    result = service.add_challenge_point(record_id, amount)

    return JSONResponse(content=result, status_code=200)


@record_router.put(
    "/comodindindin",
    response_model=Optional[RecordSchema],
)
async def comodindindin(
    record_id: UUID,
    comodindindin: int,
    db_session: Session = Depends(get_session),
):
    service = RecordService(db_session)
    result = service.comodindindin(record_id, comodindindin)

    return JSONResponse(content=result, status_code=200)


@record_router.get("/{record_id}", response_model=List[RecordSchema])
async def get_record_by_id(
    record_id: UUID,
    db_session: Session = Depends(get_session),
):
    service = RecordService(db_session)
    result = service.get_record_by_id(record_id)

    return JSONResponse(content=result, status_code=200)
