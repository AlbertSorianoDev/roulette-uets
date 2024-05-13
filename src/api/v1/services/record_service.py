from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from uuid import UUID

from src.core.schemas.record_schema import RecordSchema
from src.core.models.record_model import RecordModel


class RecordService:
    """Record service class

    Args:
        db_session (Session): Database session

    Returns:
        RecordService: Record service class
    """

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_records_by_game_id(self, game_id: UUID) -> List[dict]:
        records = self.db_session.query(RecordModel).filter_by(game_id=game_id).all()

        return [record.model_to_dict() for record in records]

    def get_record_by_game_id_and_participant_id(
        self,
        game_id: UUID,
        participant_id: UUID,
    ) -> dict | None:
        record = (
            self.db_session.query(RecordModel)
            .filter_by(game_id=game_id, participant_id=participant_id)
            .first()
        )

        return record.model_to_dict() if record else None

    def add_challenge_point(self, record_id: UUID) -> dict | None:
        try:
            record: RecordModel = self.db_session.query(RecordModel).get(record_id)

            if not record:
                return None

            record.challenge_points += 1

            self.db_session.commit()

        except SQLAlchemyError:
            self.db_session.rollback()
            return None

        return record.model_to_dict()
