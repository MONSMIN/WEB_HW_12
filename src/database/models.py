from datetime import date

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.database.db import Base

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    birthday = Column(Date)
    created_date = Column(Date, default=date.today)

