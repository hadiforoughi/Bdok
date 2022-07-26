from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.user_model import User
from app.models.product_model import Product
from app.models.basket_model import Basket
from app.api.api_v1.router import router

app = FastAPI(
    title= settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)



@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """
    
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).BDok
    
    await init_beanie(
        database=db_client,
        document_models= [
            User,
            Product,
            Basket
        ]
    )

app.include_router(router=router,prefix=settings.API_V1_STR)