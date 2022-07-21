from typing import List
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate
from uuid import UUID


class ProductServices:
    @staticmethod
    async def list_products() -> List[Product]:
        products = await Product.all().to_list()
        return products

    @staticmethod
    async def create_product(data: ProductCreate) -> Product:
        product = Product(**data.dict())
        return await product.insert()

    @staticmethod
    async def retrieve_product(product_id: UUID):
        product = await Product.find_one(Product.product_id == product_id)
        return product
    
    @staticmethod
    async def update_product(product_id: UUID, data: ProductUpdate):
        product = await ProductServices.retrieve_product(product_id)
        await product.update({"$set": data.dict(exclude_unset=True)})
        
        await product.save()
        return product
    
    @staticmethod
    async def delete_product(product_id: UUID) -> None:
        product = await ProductServices.retrieve_product(product_id)
        if product:
            await product.delete()
            
        return None
