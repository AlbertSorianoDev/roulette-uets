from sqlalchemy import Column, UUID, String
from sqlalchemy.orm import relationship
from src.core.config.database import Base


class ParticipantModel(Base):
    """Participant model class

    Args:
        participant_id (uuid): Participant unique identifier
        name (str): Participant name
        records (list): List of records

    Returns:
        ParticipantModel: A participant model object
    """

    __tablename__ = "participant"

    participant_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    name = Column(String(50), nullable=True)

    records = relationship("RecordModel", back_populates="participant")

    def __repr__(self) -> str:
        return f"<Participant(name={self.name})>"

    def model_to_dict(self) -> dict:
        return {"participant_id": self.participant_id, "name": self.name}
