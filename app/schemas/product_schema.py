from unicodedata import name
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class ProductCreate(BaseModel):
    name: str = Field(..., title='Name', max_length=55, min_length=1)
    description: str = Field(..., title='Description', max_length=755, min_length=1)
    price: Optional[int] = 0


class ProductUpdate(BaseModel):
    name: str = Field(..., title='Name', max_length=55, min_length=1)
    description: str = Field(..., title='Description', max_length=755, min_length=1)
    price: Optional[int] = 0
    
# what shows in response
class ProductOut(BaseModel):
    product_id: UUID
    name: str
    description: str
    price: int

class ProductId(BaseModel):
    product_id: UUID
