from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.orm import Session

from src.core.config.database import get_session
from src.core.schemas.subject_schema import SubjectSchema, SubjectCreateSchema
from src.api.v1.services.subject_service import SubjectService

subject_router = APIRouter(prefix="/subjects", tags=["Subjects"])


@subject_router.get("/", response_model=List[SubjectSchema])
async def get_subjects(db_session: Session = Depends(get_session)):
    service = SubjectService(db_session)
    result = service.get_subjects()

    return JSONResponse(content=result, status_code=200)


@subject_router.post("/")
async def add_subject(
    subject: SubjectCreateSchema,
    db_session: Session = Depends(get_session),
):
    service = SubjectService(db_session)
    result = service.add_subject(subject)

    if result:
        return JSONResponse(content={"ok": True, "id_subject": result}, status_code=201)
    else:
        return JSONResponse(content={"ok": False, "id_subject": None}, status_code=400)
