from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from sqlalchemy.orm import relationship
from src.core.config.database import Base
from src.core.models.question_model import QuestionModel


class OptionModel(Base):
    """Option model class

    Args:
        option_id (int): Option ID
        question_id (int): Question ID
        option_text (str): Option text
        is_correct (bool): Correct option
        question (QuestionModel): Question model

    Returns:
        OptionModel: Option model class
    """

    __tablename__ = "option"

    option_id = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(Integer, ForeignKey(QuestionModel.question_id), nullable=False)
    option_text = Column(String(510), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question = relationship("QuestionModel", back_populates="options")

    def __repr__(self) -> str:
        return self.option_text

    def model_to_dict(self) -> dict:
        return {
            "option_id": self.option_id,
            "question_id": self.question_id,
            "option_text": self.option_text,
            "is_correct": self.is_correct,
        }
