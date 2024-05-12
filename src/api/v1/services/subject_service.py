from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.models.subject_model import SubjectModel
from src.core.schemas.subject_schema import SubjectCreateSchema


class SubjectService:
    """Subject service class

    Args:
        db_session (Session): Database session

    Returns:
        SubjectService: Subject service class
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_subjects(self) -> List[dict]:
        subjects = self.db_session.query(SubjectModel).all()

        return [
            subject.model_to_dict(include_question_count=True) for subject in subjects
        ]

    def add_subject(self, subject: SubjectCreateSchema) -> int | None:
        try:
            new_subject = SubjectModel(**subject.model_dump())

            self.db_session.add(new_subject)
            self.db_session.commit()
        except SQLAlchemyError:
            return None

        return new_subject.id_subject
