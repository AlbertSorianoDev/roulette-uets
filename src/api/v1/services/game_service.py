from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.schemas.game_schema import GameCreateSchema, GameSchema, GameScoresSchema
from src.core.models.game_model import GameModel
from src.core.models.record_model import RecordModel


class GameService:
    """Game service class

    Args:
        db_session (Session): Database session

    Returns:
        GameService: Game service class
    """

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def game_with_records(self, game: GameModel) -> GameSchema:
        game_dict = game.model_to_dict()
        game_dict["records"] = [str(record.record_id) for record in game.records]

        return game_dict

    def get_games(self) -> List[GameModel]:
        games = self.db_session.query(GameModel).all()
        games_dict = []

        for game in games:
            games_dict.append(self.game_with_records(game))

        return games_dict

    def add_game(self, game: GameCreateSchema) -> GameSchema | None:
        try:
            new_game = GameModel(period_id=game.period_id, rounds=game.rounds)

            self.db_session.add(new_game)
            self.db_session.flush()

            for participant in game.participants:
                new_record = RecordModel(
                    game_id=new_game.game_id,
                    participant_id=participant,
                )
                self.db_session.add(new_record)

            self.db_session.commit()

        except SQLAlchemyError as e:
            print(e)
            self.db_session.rollback()
            return None

        return self.game_with_records(new_game)

    def get_game_scores(self, game_id: str) -> GameScoresSchema | None:
        game = (
            self.db_session.query(GameModel)
            .filter(GameModel.game_id == game_id)
            .first()
        )

        scores = []

        for record in game.records:
            participant = record.participant
            score = record.score

            score_dict = {
                "participant_id": str(participant.participant_id),
                "score": score,
            }

            scores.append(score_dict)

        return {
            "game_id": str(game_id),
            "scores": scores,
        }
