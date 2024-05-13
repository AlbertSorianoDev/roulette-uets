from pydantic import BaseModel, Field
from typing import List, Dict
from uuid import UUID


class GameCreateSchema(BaseModel):
    """Game create schema class
    Args:
        period_id (int): Period identifier
        rounds (int): Number of rounds
        participants (list): List of participants
    Returns:
        GameCreateSchema: Game create schema class
    """

    period_id: int = Field(ge=1)
    rounds: int = Field(ge=1)
    participants: List[UUID] = []

    class Config:
        json_schema_extra = {
            "example": {
                "period_id": 1,
                "rounds": 5,
                "participants": [
                    "123e4567-e89b-12d3-a456-426614174000",
                    "123e4567-e89b-12d3-a456-426614174001",
                ],
            }
        }


class GameSchema(GameCreateSchema):
    """Full game schema
    Args:
        game_id (uuid): Game unique identifier
    """

    game_id: UUID = Field(..., min_length=36, max_length=36)
    records: List[UUID] = []

    class Config:
        json_schema_extra = {
            "example": {
                "game_id": "123e4567-e89b-12d3-a456-426614174000",
                "period_id": 1,
                "rounds": 5,
                "records": [
                    "123e4567-e89b-12d3-a456-426614174000",
                    "123e4567-e89b-12d3-a456-426614174001",
                ],
            }
        }


class GameScoresSchema(BaseModel):
    """Game scores schema class
    Args:
        game_id (uuid): Game unique identifier
        scores (list): List of scores
    Returns:
        GameScoresSchema: Game scores schema class
    """

    game_id: UUID = Field(..., min_length=36, max_length=36)
    scores: List[Dict[str, str | int]] = []

    class Config:
        json_schema_extra = {
            "example": {
                "game_id": "123e4567-e89b-12d3-a456-426614174000",
                "scores": [
                    {
                        "participant_id": "123e4567-e89b-12d3-a456-426614174000",
                        "score": 100,
                    }
                ],
            }
        }
