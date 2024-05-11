from pydantic import BaseModel, Field
from typing import Optional


class QuestionSchema(BaseModel):
    """Question schema class

    Args:
        id_question (int): Question ID
        id_subject (int): Subject ID
        question_text (str): Question text
        image (bytes): Image

    Returns:
        QuestionSchema: Question schema class
    """

    id_question: int = Field(ge=1)
    id_subject: int = Field(ge=1)
    question_text: str = Field(min_length=1, max_length=510)
    image: Optional[bytes] = Field(default=None)

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id_question": 1,
                "id_subject": 1,
                "question_text": "What is the capital of Spain?",
                "image": None,
            }
        }
