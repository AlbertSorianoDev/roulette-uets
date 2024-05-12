from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from typing import List
from sqlalchemy.orm import Session
from io import BytesIO

from src.core.config.database import get_session
from src.core.schemas.question_schema import QuestionSchema, QuestionCreateSchema
from src.api.v1.services.question_service import QuestionService

question_router = APIRouter(prefix="/questions", tags=["Questions"])


@question_router.get("/", response_model=List[QuestionSchema])
async def get_questions(db_session: Session = Depends(get_session)):
    service = QuestionService(db_session)
    result = service.get_questions()

    return JSONResponse(content=result, status_code=200)


@question_router.post("/")
async def add_question(
    question: QuestionCreateSchema,
    db_session: Session = Depends(get_session),
):
    service = QuestionService(db_session)
    result = service.add_question(question)

    if result:
        return JSONResponse(
            content={"ok": True, "id_question": result},
            status_code=201,
        )
    else:
        return JSONResponse(content={"ok": False, "id_question": None}, status_code=400)


@question_router.put("/image/{question_id}")
async def add_image_to_question(
    question_id: int,
    image: UploadFile = File(...),
    db_session: Session = Depends(get_session),
):
    if not image.filename.lower().endswith(".webp"):
        raise HTTPException(
            status_code=400,
            detail="Invalid image format, only webp allowed",
        )

    service = QuestionService(db_session)
    result = service.add_image_to_question(question_id, await image.read())

    if result:
        return JSONResponse(content={"ok": True}, status_code=200)
    else:
        return JSONResponse(content={"ok": False}, status_code=400)


@question_router.get("/image/{question_id}")
async def get_image_from_question(
    question_id: int,
    db_session: Session = Depends(get_session),
):
    service = QuestionService(db_session)
    image_bytes = service.get_image_from_question(question_id)
    if image_bytes:
        return StreamingResponse(
            BytesIO(image_bytes),
            media_type="image/webp",
        )
    else:
        raise HTTPException(status_code=404, detail="Image not found")
