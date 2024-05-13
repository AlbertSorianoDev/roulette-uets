from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

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

    def get_records(self) -> List[RecordModel]:
        records = self.db_session.query(RecordModel).all()

        return [record.model_to_dict() for record in records]
