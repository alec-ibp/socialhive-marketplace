from redis_om.model import HashModel
from pydantic import BaseModel


class Product(HashModel):
    name: str
    description: str
    price: float
    quantity: int


class ProductOut(BaseModel):
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True


class OrderRequest(BaseModel):
    product_id: str
    quantity: int
