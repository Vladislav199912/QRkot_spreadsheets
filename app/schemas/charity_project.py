from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Extra, Field, PositiveInt
from app.constatnts import MAX_LENGTH


class CharityProjectBaseSchema(BaseModel, MAX_LENGTH):
    name: Optional[str] = Field(None, MAX_LENGTH)
    description: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


class CreateCharityProjectSchema(CharityProjectBaseSchema, MAX_LENGTH):
    name: str = Field(..., MAX_LENGTH)
    description: str = Field()
    full_amount: PositiveInt


class UpdateCharityProjectSchema(CharityProjectBaseSchema):
    pass


class CharityProjecDBSchema(CharityProjectBaseSchema):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True