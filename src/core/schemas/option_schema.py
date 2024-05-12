from pydantic import BaseModel, Field


class OptionCreateSchema(BaseModel):
    """Option create schema class

    Args:
        id_question (int): Question ID
        option_text (str): Option text
        is_correct (bool): Is correct
    """

    id_question: int = Field(..., ge=1)
    option_text: str = Field(..., min_length=1, max_length=510)
    is_correct: bool = Field(default=False)


class OptionSchema(OptionCreateSchema):
    """Full option schema

    Args:
        id_option (int): Option ID
    """

    id_option: int = Field(..., ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "id_option": 1,
                "id_question": 1,
                "option_text": "Madrid",
                "is_correct": True,
            }
        }
