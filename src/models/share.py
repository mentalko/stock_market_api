from enum import Enum
from datetime import date, datetime
from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, EmailStr


class CurrencyKind(str, Enum):
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'
    HK = 'HK$'

class Share(Document):
    ticker: str
    title: str
    currency: CurrencyKind 
    close_price: float 
    description: Optional[str] 

    class Config:
        schema_extra = {
            "example": {
                "title": "Tesla",
                "ticker": "TSLA",
                "currency": "USD",
                "close_price": 305.99,
                "description": "some text"
            }
        }


class ShareInfo(BaseModel):
    ticker: Optional[str]
    title: Optional[str]
    currency:  Optional[str]
    close_price: Optional[float]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Tesla",
                "ticker": "TSLA",
                "currency": "USD",
                "close_price": 305.99,
                "description": "some text"
            }
        }
    




    

# @instance.register
# class Share(Document):
#     id = fields.IntField() # fields.ObjectIdField()
#     name = fields.StrField()
#     ticker = fields.StrField()
#     currency = fields.IntField()
#     close_price = fields.FloatField(default=0.0)
#     description = fields.StrField(allow_none=True, default='')

#     class Meta:
#         collection_name = 'share'
#         collection = db.share

#     @classmethod
#     async def get(cls, id: str) -> Optional['Share']:
#         # if not ObjectId.is_valid(id):
#         #     return None

#         return await cls.find_one({'_id': id})
#         # return await cls.find_one({'_id': ObjectId(id)})

