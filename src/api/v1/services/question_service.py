from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.schemas.question_schema import QuestionCreateSchema
from src.core.models.question_model import QuestionModel


class QuestionService:
    """Question service class

    Args:
        db_session (Session): Database session

    Returns:
        QuestionService: Question service class
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_questions(self) -> List[QuestionModel]:
        questions = self.db_session.query(QuestionModel).all()

        return [question.model_to_dict() for question in questions]

    def add_question(self, question: QuestionCreateSchema) -> int | None:
        try:
            new_question = QuestionModel(**question.model_dump())

            self.db_session.add(new_question)
            self.db_session.commit()
        except SQLAlchemyError:
            return None

        return new_question.id_question

    def add_image_to_question(self, question_id, image_bytes):
        try:
            question = (
                self.db_session.query(QuestionModel)
                .filter_by(id_question=question_id)
                .first()
            )
            if question:
                question.image = image_bytes
                self.db_session.commit()
                return True

        except SQLAlchemyError:
            return False

        return False

    def get_image_from_question(self, question_id):
        question = (
            self.db_session.query(QuestionModel)
            .filter_by(id_question=question_id)
            .first()
        )
        if question:
            return question.image
        return None
