from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.models.option_model import OptionModel
from src.core.schemas.option_schema import OptionCreateSchema


class OptionService:
    """Option service class

    Args:
        db_session (Session): Database session

    Returns:
        OptionService: Option service class
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_options(self) -> List[OptionModel]:
        options = self.db_session.query(OptionModel).all()

        return [option.model_to_dict() for option in options]

    def add_option(self, option: OptionCreateSchema) -> int | None:

        try:
            new_option = OptionModel(**option.model_dump())

            self.db_session.add(new_option)
            self.db_session.commit()
        except SQLAlchemyError:
            return None

        return new_option.option_id

    def get_options_by_question_id(self, question_id: int) -> List[OptionModel]:
        options = (
            self.db_session.query(OptionModel).filter_by(question_id=question_id).all()
        )

        return [option.model_to_dict() for option in options]
