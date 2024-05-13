from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.orm import Session
from uuid import UUID

from src.core.config.database import get_session
from src.core.schemas.record_schema import (
    RecordSchema,
    RecordGameRequestSchema,
    RecordGameParticipantRequestSchema,
)
from src.api.v1.services.record_service import RecordService

record_router = APIRouter(prefix="/records", tags=["Records"])


@record_router.get("/game", response_model=List[RecordSchema])
async def get_records_by_game_id(
    request: RecordGameRequestSchema,
    db_session: Session = Depends(get_session),
):
    service = RecordService(db_session)
    result = service.get_records_by_game_id(request.game_id)

    return JSONResponse(content=result, status_code=200)


@record_router.get("/particpant_game", response_model=RecordSchema)
async def get_record_by_game_id_and_participant_id(
    request: RecordGameParticipantRequestSchema,
    db_session: Session = Depends(get_session),
):
    service = RecordService(db_session)
    result = service.get_record_by_game_id_and_participant_id(
        request.game_id,
        request.participant_id,
    )

    return JSONResponse(content=result, status_code=200)
