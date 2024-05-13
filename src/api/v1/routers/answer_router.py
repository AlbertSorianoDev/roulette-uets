from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Optional
from sqlalchemy.orm import Session

from src.core.config.database import get_session
from src.core.schemas.answer_schema import AnswerSchema, AnswerCreateSchema
from src.api.v1.services.answer_service import AnswerService

answer_router = APIRouter(prefix="/answers", tags=["Answers"])


# @answer_router.get("/", response_model=List[AnswerSchema])
# async def get_answers(db_session: Session = Depends(get_session)):
#     service = AnswerService(db_session)
#     result = service.get_answers()

#     return JSONResponse(content=result, status_code=200)


# @answer_router.post("/", response_model=Optional[AnswerSchema])
# async def add_answer(
#     answer: AnswerCreateSchema,
#     db_session: Session = Depends(get_session),
# ):
#     service = AnswerService(db_session)
#     result = service.add_answer(answer)

#     if result:
#         return JSONResponse(content=result.model_to_dict(), status_code=201)
#     else:
#         return JSONResponse(content=None, status_code=400)
