from pydantic import BaseModel, Field


class AnswerCreateSchema(BaseModel):
    """Answer create schema class
    Args:
        question_id (int): Question ID
        answer (str): Answer
    Returns:
        AnswerCreateSchema: Answer create schema class
    """

    question_id: int = Field(..., ge=1)
    answer: str = Field(min_length=1, max_length=255)

    class Config:
        json_schema_extra = {
            "example": {
                "question_id": 1,
                "answer": "This is an answer",
            }
        }


class AnswerSchema(BaseModel):
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
                "question_id": 1,
                "answer": "This is an answer",
            }
        }
