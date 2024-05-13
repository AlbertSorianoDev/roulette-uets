from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Optional
from sqlalchemy.orm import Session

from src.core.config.database import get_session
from src.core.schemas.record_schema import RecordSchema
from src.api.v1.services.record_service import RecordService

record_router = APIRouter(prefix="/records", tags=["Records"])


# @record_router.get("/", response_model=List[RecordSchema])
# async def get_records(db_session: Session = Depends(get_session)):
#     service = RecordService(db_session)
#     result = service.get_records()

#     return JSONResponse(content=result, status_code=200)
