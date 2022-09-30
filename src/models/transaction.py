from enum import Enum
from datetime import date, datetime
from typing import Optional, Any

from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field


class Transaction(Document):
    account_id: str #PydanticObjectId
    ticker: str
    cnt: int = Field(None, alias="count")
    deal_price: float
    deal_date: str

    class Config:
        schema_extra = {
            "example": {
                "account_id": "",
                "ticker": "TSLA",
                "count": 0,
                "deal_price": 1.09,
                "deal_date": "2020-09-22"
            },
        }