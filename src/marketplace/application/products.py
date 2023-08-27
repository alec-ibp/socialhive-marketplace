from __future__ import annotations

from src.marketplace.infrastructure.adapters.unit_of_work import AbstractUnitOfWork


def get_products_ids(uow: AbstractUnitOfWork) -> list[int]:
    with uow:
        products = uow.product.list()
        return [product.sku for product in products]
