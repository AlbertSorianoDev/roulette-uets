from sqlalchemy import Column, ForeignKey, Integer, Boolean, UUID
from sqlalchemy.orm import relationship
from src.core.config.database import Base


class RecordModel(Base):
    """Record model class

    Args:
        record_id (uuid): Record unique identifier
        participant_id (uuid): Participant identifier
        game_id (uuid): Game identifier
        fifty_fifty_help (bool): Fifty fifty help
        call_help (bool): Call help
        audience_help (bool): Audience help
        score (int): Score
        game (GameModel): Game object
        participant (ParticipantModel): Participant object

    Returns:
        RecordModel: A record model object
    """

    __tablename__ = "record"

    record_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    participant_id = Column(
        UUID(as_uuid=True),
        ForeignKey("participant.participant_id"),
        nullable=False,
    )
    game_id = Column(UUID(as_uuid=True), ForeignKey("game.game_id"), nullable=False)
    fifty_fifty_help = Column(Boolean, nullable=True)
    call_help = Column(Boolean, nullable=True)
    audience_help = Column(Boolean, nullable=True)
    score = Column(Integer, nullable=True)

    game = relationship("GameModel", back_populates="records")
    participant = relationship("ParticipantModel", back_populates="records")
    answers = relationship("AnswerModel", back_populates="record")

    def __repr__(self) -> str:
        return f"<Record(score={self.score})>"

    def model_to_dict(self) -> dict:
        return {
            "record_id": self.record_id,
            "participant_id": self.participant_id,
            "game_id": self.game_id,
            "fifty_fifty_help": self.fifty_fifty_help,
            "call_help": self.call_help,
            "audience_help": self.audience_help,
            "score": self.score,
        }
