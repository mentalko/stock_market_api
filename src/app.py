
from fastapi.applications import FastAPI
from fastapi_pagination import add_pagination
from src.api import router
from src.core.db import initiate_database

app = FastAPI()

@app.on_event("startup")
async def start_database():
    await initiate_database()


app.include_router(router, prefix="")
add_pagination(app)



