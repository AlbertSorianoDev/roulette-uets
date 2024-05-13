from pydantic import BaseModel, Field


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

    participant_id: str = Field(..., min_length=36, max_length=36)
    period_id: int = Field(..., ge=1)
    record_date: str = Field()
    record_value: float = Field()

    class Config:
        json_schema_extra = {
            "example": {
                "participant_id": "123e4567-e89b-12d3-a456-426614174000",
                "period_id": 1,
                "record_date": "2021-01-01",
                "record_value": 100.0,
            }
        }
