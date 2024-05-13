from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class PeriodCreateSchema(BaseModel):
    """Period create schema class
    Args:
        name (str): Period name
        init_date (str): Start date
        end_date (str): End date
        comment (str): Comment
    Returns:
        PeriodCreateSchema: Period create schema class
    """

    name: str = Field(min_length=1, max_length=50)
    init_date: date = Field()
    end_date: date = Field()
    comment: Optional[str] = Field(default=None, max_length=510)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "First Period",
                "init_date": "2021-01-01",
                "end_date": "2021-12-31",
                "comment": "This is the first period of the year",
            }
        }


class PeriodSchema(PeriodCreateSchema):
    """Full period schema

    Args:
        period_id (int): Period ID
        name (str): Period name
        init_date (str): Start date
        end_date (str): End date
    """

    period_id: int = Field(..., ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "period_id": 1,
                "name": "First Period",
                "init_date": "2021-01-01",
                "end_date": "2021-12-31",
                "comment": "This is the first period of the year",
            }
        }
