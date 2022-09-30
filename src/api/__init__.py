from fastapi import APIRouter
from . import (
    account_api,
    share_api,
    transaction_api
)

router = APIRouter()
router.include_router(account_api.router, prefix='/accounts', tags=['Account'] )
router.include_router(share_api.router, prefix='/shares', tags=['Share'])
router.include_router(transaction_api.router, prefix='/transaction', tags=['Transaction'])
