import uuid

from sqlalchemy import UUID, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.core.config.database import Base


class GameModel(Base):
    """Game model class

    Args:
        game_id (uuid): Game unique identifier
        period_id (int): Period identifier
        rounds (int): Number of rounds
        period (PeriodModel): Period object
        records (list): List of records

    Returns:
        GameModel: A game model object
    """

    __tablename__ = "game"

    game_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )
    period_id = Column(Integer, ForeignKey("period.period_id"), nullable=False)
    rounds = Column(Integer, nullable=False)

    period = relationship("PeriodModel", back_populates="games")
    records = relationship("RecordModel", back_populates="game")

    def __repr__(self) -> str:
        return f"<Game(period_id={self.period_id}, rounds={self.rounds})>"

    def model_to_dict(self) -> dict:
        return {
            "game_id": str(self.game_id),
            "period_id": self.period_id,
            "rounds": self.rounds,
        }
