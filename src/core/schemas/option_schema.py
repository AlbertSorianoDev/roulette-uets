from pydantic import BaseModel, Field
from typing import List, Optional
from src.core.schemas.question_schema import QuestionSchema


class OptionSchema(BaseModel):
    """Option schema class

    Args:
        id_option (int): Option ID
        id_question (int): Question ID
        option_text (str): Option text
        is_correct (bool): Is correct

    Returns:
        OptionSchema: Option schema class
    """

    id_option: int = Field(ge=1)
    id_question: int = Field(ge=1)
    option_text: str = Field(min_length=1, max_length=510)
    is_correct: bool = Field(default=False)
    question: Optional[QuestionSchema] = Field(default=None)

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id_option": 1,
                "id_question": 1,
                "option_text": "Madrid",
                "is_correct": True,
            }
        }
