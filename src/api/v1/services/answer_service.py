from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.schemas.answer_schema import AnswerCreateSchema, AnswerSchema
from src.core.models.answer_model import AnswerModel


class AnswerService:
    """Answer service class

    Args:
        db_session (Session): Database session

    Returns:
        AnswerService: Answer service class
    """

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_answers(self) -> List[AnswerModel]:
        answers = self.db_session.query(AnswerModel).all()

        return [answer.model_to_dict() for answer in answers]

    def add_answer(self, answer: AnswerCreateSchema) -> AnswerSchema | None:
        try:
            new_answer = AnswerModel(**answer.model_dump())

            self.db_session.add(new_answer)
            self.db_session.commit()
        except SQLAlchemyError:
            return None

        return new_answer
