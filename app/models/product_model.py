from enum import unique
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field, EmailStr

class Product(Document):
    product_id: UUID = Field(default_factory=uuid4, unique=True)
    name: Indexed(str)
    price: int
    description: Optional[str] = None

    def __repr__(self) -> str:
        return f"<Product {self.name}>"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Product):
            return self.name == other.name
        return False
    
    class Collection:
        name = "products"