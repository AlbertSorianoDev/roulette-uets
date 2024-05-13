from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Optional
from sqlalchemy.orm import Session

from src.core.config.database import get_session
from src.core.schemas.game_schema import GameSchema, GameCreateSchema
from src.api.v1.services.game_service import GameService

game_router = APIRouter(prefix="/games", tags=["Games"])


# @game_router.get("/", response_model=List[GameSchema])
# async def get_games(db_session: Session = Depends(get_session)):
#     service = GameService(db_session)
#     result = service.get_games()

#     return JSONResponse(content=result, status_code=200)


# @game_router.post("/", response_model=Optional[GameSchema])
# async def add_game(
#     game: GameCreateSchema,
#     db_session: Session = Depends(get_session),
# ):
#     service = GameService(db_session)
#     result = service.add_game(game)

#     if result:
#         return JSONResponse(content=result.model_to_dict(), status_code=201)
#     else:
#         return JSONResponse(content=None, status_code=400)
