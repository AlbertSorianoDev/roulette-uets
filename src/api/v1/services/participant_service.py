from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.core.schemas.participant_schema import (
    ParticipantCreateSchema,
    ParticipantSchema,
)
from src.core.models.participant_model import ParticipantModel


class ParticipantService:
    """Participant service class

    Args:
        db_session (Session): Database session

    Returns:
        ParticipantService: Participant service class
    """

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_participants(self) -> List[ParticipantModel]:
        participants = self.db_session.query(ParticipantModel).all()

        return [participant.model_to_dict() for participant in participants]

    def add_participant(
        self,
        participant: ParticipantCreateSchema,
    ) -> ParticipantSchema | None:
        try:
            new_participant = ParticipantModel(**participant.model_dump())

            self.db_session.add(new_participant)
            self.db_session.commit()
        except SQLAlchemyError:
            return None

        return new_participant
