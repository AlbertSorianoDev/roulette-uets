from pydantic import BaseModel, Field


class OptionCreateSchema(BaseModel):
    """Option create schema class

    Args:
        question_id (int): Question ID
        option_text (str): Option text
        is_correct (bool): Is correct
    """

    question_id: int = Field(..., ge=1)
    option_text: str = Field(..., min_length=1, max_length=510)
    is_correct: bool = Field(default=False)


class OptionSchema(OptionCreateSchema):
    """Full option schema

    Args:
        option_id (int): Option ID
    """

    option_id: int = Field(..., ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "option_id": 1,
                "question_id": 1,
                "option_text": "Madrid",
                "is_correct": True,
            }
        }
