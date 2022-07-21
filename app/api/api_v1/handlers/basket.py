from fastapi import APIRouter
from app.schemas.basket_schema import BasketOut, BasketCreate, BasketUpdate, BasketList
from app.services.basket_service import BasketService
from app.models.basket_model import Basket
from uuid import UUID
from typing import List


basket_router = APIRouter()

@basket_router.get('/',summary="get all basket",response_model=List[BasketList])
async def list():
    return await BasketService.list_baskets()

@basket_router.post('/create',summary="create new basket", response_model=Basket)
async def crete_basket(data: BasketCreate):
    return await BasketService.create_basket(data)

@basket_router.get('/{basket_id}', summary="Get a basket by basket_id", response_model=BasketOut)
async def retrieve(basket_id: UUID):
    return await BasketService.retrieve_basket(basket_id)


@basket_router.put('/{basket_id}', summary="Update basket by basket_id", response_model=BasketOut)
async def update(basket_id: UUID, data: BasketUpdate):
    return await BasketService.update_basket(basket_id, data)


@basket_router.delete('/{basket_id}', summary="Delete basket by basket_id")
async def delete(basket_id: UUID):
    await BasketService.delete_basket(basket_id)
    return None