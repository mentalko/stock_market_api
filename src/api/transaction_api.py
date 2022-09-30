import json
import logging
from typing import List, Optional, Any
from fastapi import APIRouter, Body, HTTPException
from fastapi import Depends, Response, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
from fastapi_pagination import Page, add_pagination, paginate

from ..models.transaction import Transaction
from ..services.tansactions_service import TransactionsService

from beanie import PydanticObjectId

log = logging.getLogger(__name__)

router = APIRouter()


@router.get("/all", response_model=Page, status_code=status.HTTP_200_OK)
async def all_transactions(service: TransactionsService = Depends()):
    response = await service.get_all_transactions()
    return paginate(response)


@router.get("", response_model=Any, status_code=status.HTTP_200_OK)
async def transaction_by_account(account_id: PydanticObjectId,
                                 service: TransactionsService = Depends()):
    response = await service.get_transactions_by_account(account_id)
    return response


# ======================= POST =======================
@router.post('',
             response_model=Any,
             status_code=status.HTTP_201_CREATED)
async def create_transaction(payload: Transaction,
                         service: TransactionsService = Depends()):
    response = await service.create_transaction(payload=payload)
    return response
