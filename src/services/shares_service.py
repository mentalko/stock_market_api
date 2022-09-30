import json
from typing import List, Optional
from bson import json_util
from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from src.models.share import Share
from src.models.account import Account


class SharesService:
    def __init__(self):
        pass

    async def get_all_shares(self):
        shares = await Share.find().to_list()
        return shares

    async def get_shares_by_id(self, id):
        share = await Share.get(document_id=id)
        if not share:
            raise HTTPException(404)
        return share

    async def get_shares_by_ticker(self, ticker):
        share = await Share.find_one(Share.ticker == ticker)
        if not share:
            raise HTTPException(404)
        return share

    async def get_shares_search(self, id):
        pass

    

     
