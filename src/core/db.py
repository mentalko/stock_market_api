from src.core import config
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from beanie import Document, Indexed, init_beanie

from ..models.account import Account
from ..models.share import Share
from ..models.transaction import Transaction


async def initiate_database():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client['stock'], document_models=[Account, Share, Transaction])

