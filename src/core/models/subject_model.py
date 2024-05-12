from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.core.config.database import Base


class SubjectModel(Base):
    """Subjecy model class

    Args:
        subject_id(int): Subject ID
        name (str): Subject name
        questions (list): List of questions
        question_count (int): Number of questions

    Returns:
        SubjectModel: Subject model class
    """

    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    questions = relationship("QuestionModel", back_populates="subject")

    @property
    def question_count(self) -> int:
        return len(self.questions)

    def __repr__(self) -> str:
        return self.name

    def model_to_dict(self, include_question_count=False) -> dict:
        data = {
            "subject_id": self.subject_id,
            "name": self.name,
        }

        if include_question_count:
            data["question_count"] = self.question_count

        return data
