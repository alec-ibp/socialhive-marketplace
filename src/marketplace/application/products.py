from __future__ import annotations

from src.marketplace.domain.models import Product
from src.marketplace.infrastructure.adapters.unit_of_work import AbstractUnitOfWork


def get_products_ids(uow: AbstractUnitOfWork) -> list[int]:
    with uow:
        return uow.product.list()


def add_new_product(uow: AbstractUnitOfWork, new_product: Product) -> None:
    with uow:
        created_product = uow.product.add(new_product)
        uow.commit()
        return created_product
