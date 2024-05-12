from pydantic import BaseModel, Field
from typing import Optional

from pydantic import BaseModel, Field
from typing import Optional


class SubjectCreateSchema(BaseModel):
    """Subject create schema class

    Args:
        name (str): Subject name
    """

    name: str = Field(..., min_length=1, max_length=50)


class SubjectSchema(SubjectCreateSchema):
    """Full subject schema

    Args:
        id_subject (int): Subject ID
        question_count (int): Number of questions
    """

    id_subject: int = Field(ge=1)
    question_count: Optional[int] = Field(default=None, ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "id_subject": 1,
                "name": "Math",
                "question_count": 10,
            }
        }
