from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.api.v1.routers.subject_router import subject_router
from src.api.v1.routers.question_router import question_router
from src.api.v1.routers.option_router import option_router

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(subject_router)
api_v1_router.include_router(question_router)
api_v1_router.include_router(option_router)


@api_v1_router.get("/", tags=["Index"])
async def index():
    return JSONResponse(
        content={"message": "Welcome to Roulette UETS API v1"}, status_code=200
    )
