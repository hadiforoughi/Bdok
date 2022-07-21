from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from app.models.product_model import Product
from app.schemas.product_schema import ProductId
from typing import List

class BasketCreate(BaseModel):
    items: List[ProductId]
    status: Optional[bool] = False
    product_count: int = 0


class BasketUpdate(BaseModel):
    items: List[ProductId]
    status: Optional[bool] = False
    product_count: int = 0
    
# what shows in response
class BasketOut(BaseModel):
    items: List[ProductId]
    basket_id: UUID
    status: bool
    created_at: datetime
    updated_at: datetime
    product_count: int

class BasketList(BaseModel):
    # items: List[ProductId]
    basket_id: UUID
    status: bool
    created_at: datetime
    updated_at: datetime
    product_count: int
 