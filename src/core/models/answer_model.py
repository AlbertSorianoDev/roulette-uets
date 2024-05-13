from sqlalchemy import Column, ForeignKey, Integer, UUID
from sqlalchemy.orm import relationship
from src.core.config.database import Base


class AnswerModel(Base):
    """Answer model class

    Args:
        answer_id (int): Answer identifier
        option_id (int): Option identifier
        record_id (int): Record identifier
        record (RecordModel): Record object

    Returns:
        AnswerModel: An answer model object
    """

    __tablename__ = "answer"

    answer_id = Column(Integer, primary_key=True, nullable=False)
    option_id = Column(Integer, ForeignKey("option.option_id"), nullable=False)
    record_id = Column(UUID, ForeignKey("record.record_id"), nullable=False)

    record = relationship("RecordModel", back_populates="answers")

    def __repr__(self) -> str:
        return f"<Answer(answer_id={self.answer_id})>"

    def model_to_dict(self) -> dict:
        return {
            "answer_id": self.answer_id,
            "option_id": self.option_id,
            "record_id": str(self.record_id),
        }
