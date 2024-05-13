from pydantic import BaseModel, Field


class GameCreateSchema(BaseModel):
    """Game create schema class
    Args:
        period_id (int): Period identifier
        rounds (int): Number of rounds
    Returns:
        GameCreateSchema: Game create schema class
    """

    period_id: int = Field(ge=1)
    rounds: int = Field(ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "period_id": 1,
                "rounds": 5,
            }
        }


class GameSchema(GameCreateSchema):
    """Full game schema

    Args:
        game_id (uuid): Game unique identifier
    """

    game_id: str = Field(..., min_length=36, max_length=36)

    class Config:
        json_schema_extra = {
            "example": {
                "game_id": "123e4567-e89b-12d3-a456-426614174000",
                "period_id": 1,
                "rounds": 5,
            }
        }
