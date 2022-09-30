import json
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from beanie import Document, Indexed, init_beanie

from src.models.share import Share
from src.models.account import Account
from src.models.transaction import Transaction
from pydantic import BaseModel, Field



class  OutputItem(BaseModel):
    id: str = Field(None, alias="_id")
    count: int
    avg_price: float
    total: float


async def get_accounts_shares(account_id):
    user_shares = await Transaction.find(Transaction.account_id == account_id).aggregate(
        [{"$group": {
                    "_id": "$ticker",
                    "count": {"$sum": "$count"},
                    "avg_price": {"$avg":"$deal_price"}
                    
                    }},
        {"$project": {
                    "_id": 1, "count": 1, "avg_price": 1,
                    "total": { "$multiply": [ "$count", "$avg_price" ] }  
                    }
        }
                    ],
                    projection_model=OutputItem
    ).to_list()
                                         
    return user_shares


class AccountsService:

    def __init__(self):
        pass

    async def get_accounts_list(self):
        accounts = await Account.find().to_list()
        return accounts

    async def get_account_by_id(self, id):
        account = await Account.get(document_id=id)
        if not account:
            raise HTTPException(404)

        share_list = await get_accounts_shares(str(id))
        total_sum = sum(share.total for share in share_list)

        account_dict = account.dict()
        account_dict["balance"] = account.deposited_usd - total_sum
        account_dict["share_list"] = share_list
        account_dict["profitability"] = (account.deposited_usd - total_sum ) / account.deposited_usd * 100

        return account_dict

    async def topup_deposite(self, id, value):
        account = await Account.get(id)
        if not account:
            raise HTTPException(404)

        await account.inc({Account.deposited_usd: value})
        return account

    async def create_account(self, payload):
        account = Account(**payload.dict())
        return await account.insert()
