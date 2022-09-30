import json
from typing import List, Optional
from bson import json_util
from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from src.models.transaction import Transaction
from src.models.account import Account


class TransactionsService:

    def __init__(self):
        pass

    async def get_all_transactions(self):
        transactions = await Transaction.find().to_list()
        return transactions

    async def get_transactions_by_account(self, id):
        transactions = await Transaction.find(Transaction.account_id == str(id)
                                              ).to_list()
        if not transaction:
            raise HTTPException(404)
        return transactions

    async def create_transaction(self, payload):
        transaction = Transaction(**payload.dict())
        return await transaction.insert()
