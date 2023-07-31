from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class ContactSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    created_date: Optional[date]

    def __init__(self, **data):
        super().__init__(**data)
        self.created_date = date.today()


class ContactUpdateSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    update_date: Optional[date]

    def __init__(self, **data):
        super().__init__(**data)
        self.update_date = date.today()


class ContactResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date

    class Config:
        from_attributes = True
