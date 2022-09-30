import json
from typing import List, Any, Optional
from fastapi import APIRouter, Body, HTTPException
from fastapi import Depends, Response, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
from fastapi_pagination import Page, add_pagination, paginate
from fastapi.encoders import jsonable_encoder

from ..models.account import Account, AccountInfo  #, AccountShares, AccountBalance
from ..services.accounts_service import AccountsService

from beanie import PydanticObjectId

router = APIRouter()


@router.get("/all",
            summary="Get all Accounts list",
            response_model=Page,
            status_code=status.HTTP_200_OK)
async def all_accounts(service: AccountsService = Depends()):
    try:
        response = await service.get_accounts_list()
        return paginate(response)

    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


@router.get('',
            summary="Get Account Info by ID",
            response_model=AccountInfo,
            status_code=status.HTTP_200_OK)
async def get_account_by_id(id: PydanticObjectId,
                            service: AccountsService = Depends()):
    try:
        response = await service.get_account_by_id(id)
        return response

    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


@router.get('/topup_deposite',
            summary="Topup Account balance",
            response_model=Any,
            status_code=status.HTTP_200_OK)
async def topup_account(value: float,
                        id: PydanticObjectId,
                        service: AccountsService = Depends()):
    try:
        response = await service.topup_deposite(id, value)
        return response

    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e


# ======================= POST =======================
@router.post("/create",
             summary="Creates an Account",
             response_model=Account,
             status_code=status.HTTP_201_CREATED)
async def create_account(payload: Account,
                         service: AccountsService = Depends()):
    try:
        response = await service.create_account(payload=payload)
        return response

    except (HTTPException, Exception) as e:
        # TODO handel 400 401 403 405 409
        raise e
