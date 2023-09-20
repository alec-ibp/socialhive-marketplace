from __future__ import annotations

from redis_om.model import NotFoundError

from src.marketplace.domain.models import Product
from src.marketplace.domain.interfaces import AbstractRepository


# redis repository
class ProductRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def list(self, only_ids: bool) -> list[Product | str]:
        if only_ids:
            return Product.all_pks()
        return [self.get(product_id).dict() for product_id in Product.all_pks()]

    def add(self, product: Product) -> Product:
        return product.save()

    def get(self, product_id: int) -> Product:
        try:
            return Product.get(product_id)
        except NotFoundError:
            return None

    def delete(self, product_id: int) -> None:
        return Product.delete(product_id)

    def update_quantity(self, product_id: int, quantity: int) -> Product | None:
        product: Product | None = self.get(product_id)
        if product:
            product.quantity = quantity
            product.save()
            return product
