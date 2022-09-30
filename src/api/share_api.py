import json
import logging
from typing import List, Optional
from fastapi import APIRouter, Body, HTTPException
from fastapi import Depends, Response, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
from fastapi_pagination import Page, add_pagination, paginate

from ..models.share import Share, ShareInfo
from ..models.transaction import Transaction
from ..services.shares_service import SharesService
from ..services.tansactions_service import TransactionsService

from beanie import PydanticObjectId

log = logging.getLogger(__name__)

router = APIRouter()


@router.get("/all",
            summary="All Shares list",
            response_model=Page,
            status_code=status.HTTP_200_OK)
async def all_shares(service: SharesService = Depends()):
    response = await service.get_all_shares()
    return paginate(response)


@router.get('',
            summary="Get share by ID or ticker",
            response_model=ShareInfo,
            status_code=status.HTTP_200_OK)
async def get_share(id: Optional[PydanticObjectId] = None,
                    ticker: Optional[str] = None,
                    service: SharesService = Depends()):
    if id:
        response = await service.get_shares_by_id(id)
    elif ticker:
        response = await service.get_shares_by_ticker(ticker)
    return response



# ======================= POST =======================
@router.post("/buy",
             summary="Buy shares",
             response_model=Transaction,
             status_code=status.HTTP_201_CREATED)
async def create_account(payload: Transaction,
                         service: TransactionsService = Depends()):
    try:
        response = await service.create_transaction(payload=payload)
        return response

    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e
