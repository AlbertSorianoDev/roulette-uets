from pydantic import BaseModel, Field
from typing import Optional


class SubjectSchema(BaseModel):
    """Subject schema class

    Args:
        id_subject (int): Subject ID
        name (str): Subject name
        question_count (int): Number of questions

    Returns:
        SubjectSchema: Subject schema class
    """

    id_subject: int = Field(ge=1)
    name: str = Field(min_length=1, max_length=50)
    question_count: Optional[int] = Field(default=None, ge=0)

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id_subject": 1,
                "name": "Math",
                "question_count": 10,
            }
        }
