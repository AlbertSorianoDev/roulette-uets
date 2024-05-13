from pydantic import BaseModel, Field
from uuid import UUID


class AnswerCreateSchema(BaseModel):
    """Answer create schema class
    Args:
        question_id (int): Question ID
        answer (str): Answer
    Returns:
        AnswerCreateSchema: Answer create schema class
    """

    option_id: int = Field(ge=1)
    record_id: UUID

    class Config:
        json_schema_extra = {
            "example": {
                "option_id": 1,
                "record_id": "123e4567-e89b-12d3-a456-426614174000",
            }
        }


class AnswerSchema(AnswerCreateSchema):
    """Answer schema class
    Args:
        answer_id (int): Answer ID
        question_id (int): Question ID
        answer (str): Answer
    Returns:
        AnswerSchema: Answer schema class
    """

    answer_id: int = Field(ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "answer_id": 1,
                "option_id": 1,
                "record_id": "123e4567-e89b-12d3-a456-426614174000",
            }
        }
