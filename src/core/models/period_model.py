from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship
from src.core.config.database import Base


class PeriodModel(Base):
    """Period model class

    Args:
        period_id (int): Period identifier
        name (str): Period name
        init_date (date): Period initial date
        end_date (date): Period end date
        comment (str): Period comment
        games (list): List of games

    Returns:
        PeriodModel: A period model object
    """

    __tablename__ = "period"

    period_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=True)
    init_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    comment = Column(String(510), nullable=True)

    games = relationship("GameModel", back_populates="period")

    def __repr__(self) -> str:
        return f"<Period(name={self.name})>"

    def model_to_dict(self) -> dict:
        return {
            "period_id": self.period_id,
            "name": self.name,
            "init_date": self.init_date,
            "end_date": self.end_date,
            "comment": self.comment,
        }
