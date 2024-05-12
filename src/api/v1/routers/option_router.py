from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.orm import Session

from src.core.config.database import get_session
from src.core.schemas.option_schema import OptionCreateSchema, OptionSchema
from src.api.v1.services.option_service import OptionService

option_router = APIRouter(prefix="/options", tags=["Options"])


@option_router.get("/", response_model=List[OptionSchema])
async def get_options(db_session: Session = Depends(get_session)):
    service = OptionService(db_session)
    result = service.get_options()

    return JSONResponse(content=result, status_code=200)


@option_router.post("/")
async def add_option(
    option: OptionCreateSchema,
    db_session: Session = Depends(get_session),
):
    service = OptionService(db_session)
    result = service.add_option(option)

    if result:
        return JSONResponse(content={"ok": True, "option_id": result}, status_code=201)
    else:
        return JSONResponse(content={"ok": False, "option_id": None}, status_code=400)


@option_router.get("/{question_id}", response_model=List[OptionSchema])
def get_options_by_question_id(
    question_id: int,
    db_session: Session = Depends(get_session),
):
    service = OptionService(db_session)
    result = service.get_options_by_question_id(question_id)

    return JSONResponse(content=result, status_code=200)
