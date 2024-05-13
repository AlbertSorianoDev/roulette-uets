from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Optional
from sqlalchemy.orm import Session

from src.core.config.database import get_session
from src.core.schemas.period_schema import PeriodSchema, PeriodCreateSchema
from src.api.v1.services.period_service import PeriodService

period_router = APIRouter(prefix="/periods", tags=["Periods"])


@period_router.get("/", response_model=List[PeriodSchema])
async def get_periods(db_session: Session = Depends(get_session)):
    service = PeriodService(db_session)
    result = service.get_periods()

    return JSONResponse(content=result, status_code=200)


@period_router.post("/", response_model=Optional[PeriodSchema])
async def add_period(
    period: PeriodCreateSchema,
    db_session: Session = Depends(get_session),
):
    service = PeriodService(db_session)
    result = service.add_period(period)

    if result:
        return JSONResponse(content=result, status_code=201)
    else:
        return JSONResponse(content=None, status_code=400)
