from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.schemas.answer_schema import AnswerCreateSchema
from src.core.models.answer_model import AnswerModel
from src.core.models.record_model import RecordModel


class AnswerService:
    """Answer service class

    Args:
        db_session (Session): Database session

    Returns:
        AnswerService: Answer service class
    """

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_answers(self) -> List[dict]:
        answers = self.db_session.query(AnswerModel).all()

        return [answer.model_to_dict() for answer in answers]

    def add_answer(self, answer: AnswerCreateSchema) -> dict | None:
        try:
            new_answer: AnswerModel = AnswerModel(**answer.model_dump())

            self.db_session.add(new_answer)
            self.db_session.flush()

            record_model: RecordModel = self.db_session.query(RecordModel).get(
                answer.record_id
            )

            if answer.is_correct:
                record_model.score += 1

                self.db_session.flush()

            self.db_session.commit()

        except SQLAlchemyError:
            self.db_session.rollback()
            return None

        return record_model.model_to_dict()
