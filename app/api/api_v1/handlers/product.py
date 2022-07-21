from fastapi import APIRouter
from app.schemas.product_schema import ProductOut, ProductCreate, ProductUpdate
from app.services.product_service import ProductServices
from app.models.product_model import Product
from uuid import UUID
from typing import List


product_router = APIRouter()

@product_router.get('/',summary="get all product",response_model=List[ProductOut])
async def list():
    return await ProductServices.list_products()

@product_router.post('/create',summary="create new product", response_model=Product)
async def crete_product(data: ProductCreate):
    return await ProductServices.create_product(data)

@product_router.get('/{product_id}', summary="Get a product by product_id", response_model=ProductOut)
async def retrieve(product_id: UUID):
    return await ProductServices.retrieve_product(product_id)


@product_router.put('/{product_id}', summary="Update product by product_id", response_model=ProductOut)
async def update(product_id: UUID, data: ProductUpdate):
    return await ProductServices.update_product(product_id, data)


@product_router.delete('/{product_id}', summary="Delete product by product_id")
async def delete(product_id: UUID):
    await ProductServices.delete_product(product_id)
    return None