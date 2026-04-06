from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class RecordCreate(BaseModel):
    amount: float = Field(..., gt=0)
    type: str
    category: str
    notes: Optional[str]

    @validator("type")
    def validate_type(cls, v):
        if v not in ["income", "expense"]:
            raise ValueError("type must be 'income' or 'expense'")
        return v

    @validator("category")
    def validate_category(cls, v):
        if not v.strip():
            raise ValueError("category cannot be empty")
        return v


class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: datetime
    notes: Optional[str]

    class Config:
        from_attributes = True