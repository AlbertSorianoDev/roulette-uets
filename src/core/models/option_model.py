from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from sqlalchemy.orm import relationship
from src.core.config.database import Base


class OptionModel(Base):
    """Option model class

    Args:
        id_option (int): Option ID
        question_id (int): Question ID
        option_text (str): Option text
        is_correct (bool): Correct option
        question (QuestionModel): Question model

    Returns:
        OptionModel: Option model class
    """

    __tablename__ = "option"

    id_option = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id_question"), nullable=False)
    option_text = Column(String(510), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question = relationship("QuestionModel", back_populates="options")

    def __repr__(self) -> str:
        return self.option_text

    def model_to_dict(self) -> dict:
        return {
            "id_option": self.id_option,
            "question_id": self.question_id,
            "option_text": self.option_text,
            "is_correct": self.is_correct,
        }
