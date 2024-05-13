from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.schemas.period_schema import PeriodCreateSchema, PeriodSchema
from src.core.models.period_model import PeriodModel


class PeriodService:
    """Period service class

    Args:
        db_session (Session): Database session

    Returns:
        PeriodService: Period service class
    """

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_periods(self) -> List[PeriodModel]:
        periods = self.db_session.query(PeriodModel).all()

        return [period.model_to_dict() for period in periods]

    def add_period(self, period: PeriodCreateSchema) -> dict | None:
        try:
            new_period = PeriodModel(**period.model_dump())

            self.db_session.add(new_period)
            self.db_session.commit()
        except SQLAlchemyError:
            return None

        return new_period.model_to_dict()
