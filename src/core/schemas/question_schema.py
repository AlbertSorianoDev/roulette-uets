from pydantic import BaseModel, Field
from typing import Optional


class QuestionCreateSchema(BaseModel):
    """Question create schema class
    Args:
        subject_id (int): Subject ID
        question_text (str): Question text
        image (bytes): Image
    Returns:
        QuestionCreateSchema: Question create schema class
    """

    subject_id: int = Field(ge=1)
    question_text: str = Field(max_length=510)


class QuestionSchema(QuestionCreateSchema):
    """Full question schema

    Args:
        question_id (int): Question ID
        have_image (bool): Have image
    """

    question_id: int = Field(..., ge=1)
    have_image: bool = Field(default=False)

    class Config:
        json_schema_extra = {
            "example": {
                "question_id": 1,
                "subject_id": 1,
                "question_text": "What is the capital of Spain?",
                "have_image": False,
            }
        }
