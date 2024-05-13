from pydantic import BaseModel, Field
from uuid import UUID


class RecordSchema(BaseModel):
    """Record schema class
    Args:
        participant_id (str): Participant unique identifier
        period_id (int): Period ID
        record_date (str): Record date
        record_value (float): Record value
    Returns:
        RecordSchema: Record schema class
    """

    record_id: UUID = Field(..., min_length=36, max_length=36)
    participant_id: UUID = Field(..., min_length=36, max_length=36)
    game_id: UUID = Field(..., min_length=36, max_length=36)
    fifty_fifty_help: bool = Field(default=True)
    call_help: bool = Field(default=True)
    audience_help: bool = Field(default=True)
    score: int = Field(default=None, ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "record_id": "123e4567-e89b-12d3-a456-426614174000",
                "participant_id": "123e4567-e89b-12d3-a456-426614174000",
                "game_id": "123e4567-e89b-12d3-a456-426614174000",
                "fifty_fifty_help": True,
                "call_help": True,
                "audience_help": True,
                "score": 100,
            }
        }
