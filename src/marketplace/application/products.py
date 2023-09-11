from __future__ import annotations

from src.marketplace.domain.models import Product
from src.marketplace.infrastructure.adapters.unit_of_work import AbstractUnitOfWork


def get_products(uow: AbstractUnitOfWork, only_ids: bool) -> list[int]:
    with uow:
        return uow.product.list(only_ids=only_ids)


def add_new_product(uow: AbstractUnitOfWork, new_product: Product) -> None:
    with uow:
        created_product = uow.product.add(new_product)
        uow.commit()
        return created_product


def get_product(uow: AbstractUnitOfWork, product_id: int) -> Product:
    with uow:
        return uow.product.get(product_id)


def delete_product(uow: AbstractUnitOfWork, product_id: int) -> None:
    with uow:
        uow.product.delete(product_id)
        uow.commit()
