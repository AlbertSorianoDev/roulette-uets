from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import Optional
from sqlalchemy.orm import Session
from uuid import UUID

from src.core.config.database import get_session
from src.core.schemas.answer_schema import AnswerCreateSchema, AnswerSchema
from src.core.schemas.record_schema import RecordSchema
from src.api.v1.services.answer_service import AnswerService

answer_router = APIRouter(prefix="/answers", tags=["Answers"])


@answer_router.get("/{record_id}", response_model=list[AnswerSchema])
async def get_answers_by_record(
    record_id: UUID, db_session: Session = Depends(get_session)
):
    service = AnswerService(db_session)
    return service.get_answers_by_record(record_id)


@answer_router.post("", response_model=Optional[RecordSchema])
async def add_answer(
    answer: AnswerCreateSchema,
    db_session: Session = Depends(get_session),
):
    service = AnswerService(db_session)
    result = service.add_answer(answer)

    if result:
        return JSONResponse(content=result, status_code=201)
    else:
        return JSONResponse(content=None, status_code=400)
