from typing import List
from uuid import UUID
from app.models.basket_model import Basket
from app.models.product_model import Product
from app.schemas.basket_schema import BasketCreate, BasketUpdate

class BasketService:
    @staticmethod
    async def list_baskets() -> List[Basket]:
        baskets = await Basket.all().to_list()
        return baskets
    
    @staticmethod
    async def create_basket(data: BasketCreate) -> Basket:
        product = await Product.find_one(Product.product_id == data.items.product_id)
        status = data.status
        product_count = data.product_count
        basket = Basket(items=product,status=status,product_count=product_count)
        return await basket.insert()
    
    @staticmethod
    async def retrieve_basket(basket_id: UUID):
        basket = await Basket.find_one(Basket.basket_id == basket_id)
        return basket
    
    @staticmethod
    async def update_basket(basket_id: UUID, data: BasketUpdate):
        basket = await BasketService.retrieve_basket(basket_id)
        product = await Product.find_one(Product.product_id == data.items.product_id)
        status = data.status
        product_count = data.product_count
        data_dic = {
            'items': product,
            'status': status,
            'product_count': product_count
        }
        await basket.update({"$set": data_dic})
        await basket.save()
        return basket
    
    @staticmethod
    async def delete_basket(basket_id: UUID) -> None:
        basket = await BasketService.retrieve_basket(basket_id)
        if basket:
            await basket.delete()
            
        return None