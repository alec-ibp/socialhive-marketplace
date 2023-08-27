from redis_om.model import HashModel


class Product(HashModel):
    name: str
    description: str
    price: float
    quantity: int
