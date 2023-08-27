from __future__ import annotations

from abc import ABC, abstractmethod

from src.marketplace.domain.models import Product


class AbstractRepository(ABC):
    @abstractmethod
    def list(self) -> list[Product]:
        raise NotImplementedError


# redis repository
class ProductRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def list(self) -> list[Product]:
        return Product.all_pks()
