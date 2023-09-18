from dataclasses import dataclass


@dataclass
class Event:
    pass


@dataclass
class CreateOrder(Event):
    product_id: str
    price: float
    fee: float
    total: float
