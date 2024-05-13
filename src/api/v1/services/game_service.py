from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.schemas.game_schema import GameCreateSchema, GameSchema
from src.core.models.game_model import GameModel


class GameService:
    """Game service class

    Args:
        db_session (Session): Database session

    Returns:
        GameService: Game service class
    """

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_games(self) -> List[GameModel]:
        games = self.db_session.query(GameModel).all()

        return [game.model_to_dict() for game in games]

    def add_game(self, game: GameCreateSchema) -> GameSchema | None:
        try:
            new_game = GameModel(**game.model_dump())

            self.db_session.add(new_game)
            self.db_session.commit()
        except SQLAlchemyError:
            return None

        return new_game
