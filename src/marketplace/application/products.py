from __future__ import annotations

from fastapi import status  # TODO should be a custom exception
from fastapi.exceptions import HTTPException  # TODO should be a custom exception

from src.marketplace.domain.models import Product
from src.marketplace.domain.events import CreateOrder
from src.marketplace.application.messagebus import handler
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


def create_order(uow: AbstractUnitOfWork, product_id: int, quantity: float) -> None:
    with uow:
        product: Product = uow.product.get(product_id)

    if product.quantity < quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough products in stock")
    handler(CreateOrder(
        product_id=product.pk,
        price=product.price,
        fee=0.2 * product.price,
        total=1.2 * product.price
    ))
