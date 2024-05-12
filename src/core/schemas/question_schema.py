from pydantic import BaseModel, Field
from typing import Optional


class QuestionCreateSchema(BaseModel):
    """Question create schema class
    Args:
        id_subject (int): Subject ID
        question_text (str): Question text
        image (bytes): Image
    Returns:
        QuestionCreateSchema: Question create schema class
    """

    id_subject: int = Field(ge=1)
    question_text: str = Field(max_length=510)


class QuestionSchema(QuestionCreateSchema):
    """Full question schema

    Args:
        id_question (int): Question ID
        have_image (bool): Have image
    """

    id_question: int = Field(..., ge=1)
    have_image: bool = Field(default=False)

    class Config:
        json_schema_extra = {
            "example": {
                "id_question": 1,
                "id_subject": 1,
                "question_text": "What is the capital of Spain?",
                "have_image": False,
            }
        }
