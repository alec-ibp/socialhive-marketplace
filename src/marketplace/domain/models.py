from redis_om import HashModel


class Product(HashModel):
    name: str
    description: str
    price: float
    quantity: int
