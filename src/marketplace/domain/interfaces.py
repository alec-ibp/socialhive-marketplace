from __future__ import annotations

from abc import ABC, abstractmethod
from .models import Product


class AbstractRepository(ABC):
    @abstractmethod
    def list(self, only_ids: bool) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    def add(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def get(self, product_id: int) -> Product:
        raise NotImplementedError

    @abstractmethod
    def delete(self, product_id: int) -> None:
        raise NotImplementedError
