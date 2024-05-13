from uuid import UUID
from pydantic import BaseModel, Field


class ParticipantCreateSchema(BaseModel):
    """Participant create schema class
    Args:
        name (str): Participant name
    Returns:
        ParticipantCreateSchema: Participant create schema class
    """

    name: str = Field(min_length=1, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
            }
        }


class ParticipantSchema(ParticipantCreateSchema):
    """Full participant schema

    Args:
        participant_id (uuid): Participant unique identifier
    """

    participant_id: UUID = Field(..., min_length=36, max_length=36)

    class Config:
        json_schema_extra = {
            "example": {
                "participant_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "John Doe",
            }
        }
