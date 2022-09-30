from datetime import date, datetime
from typing import Optional, Any, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

from .share import Share


class Account(Document):
    full_name: str
    email: EmailStr
    hashed_password: str
    registration_date: str
    deposited_usd: float
    share_list: Optional[List]

    class Settings:
        name = 'Account'

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Cotton Joe",
                "email": "joe@gmail.com",
                "hashed_password": "hashed_password",
                "registration_date": "2010-09-23",
                "deposited_usd": 2000.00,
                "share_list": []
            }
        }


class AccountInfo(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr]
    hashed_password: Optional[str]
    registration_date: Optional[str]
    balance: Optional[float]
    deposited_usd: Optional[float]
    share_list: Optional[List]
    balance: Optional[float]
    profitability: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Cotton Joe update",
                "email": "joe@gmail.com",
                "hashed_password": "hashed_password",
                "registration_date": "1975-01-01",
                "deposited_usd": 2000.00,
                "share_list": []
            }
        }
