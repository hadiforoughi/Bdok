from enum import unique
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field, EmailStr
from app.models.product_model import Product
from typing import List

class Basket(Document):
    basket_id: UUID = Field(default_factory=uuid4, unique=True)
    items: List[Product]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    status: bool = False
    product_count: int = 0

    def __repr__(self) -> str:
        return f"<Basket {self.basket_id}>"

    def __str__(self) -> str:
        return self.basket_id

    def __hash__(self) -> int:
        return hash(self.basket_id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Basket):
            return self.basket_id == other.basket_id
        return False

    @before_event([Replace, Insert])
    def update_update_at(self):
        self.updated_at = datetime.utcnow()
        
    
    class Collection:
        name = "Baskets"