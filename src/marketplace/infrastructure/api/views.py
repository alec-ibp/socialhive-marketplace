from __future__ import annotations

from typing import Union

from fastapi import APIRouter, status

from src.marketplace.domain.models import Product, ProductOut
from src.marketplace.application.products import get_products, add_new_product, get_product, delete_product
from src.marketplace.infrastructure.adapters.unit_of_work import RedisUnitOfWork


router: APIRouter = APIRouter()


@router.get(
    path="/products",
    response_model=dict[str, list[Union[ProductOut, str]]],
    status_code=status.HTTP_200_OK
)
async def get_all(only_ids: bool = True) -> dict[str, list[Union[ProductOut, str]]]:
    print(get_products(RedisUnitOfWork(), only_ids=only_ids))
    return {"results": get_products(RedisUnitOfWork(), only_ids=only_ids)}


@router.post(
    path="/products",
    response_model=Product,
    status_code=status.HTTP_201_CREATED
)
async def create(product: Product) -> Product:
    new_product: Product = add_new_product(RedisUnitOfWork(), product)
    return new_product


@router.get(
    path="/products/{product_id}/details",
    response_model=Product,
    status_code=status.HTTP_200_OK
)
async def get(product_id: str) -> Product:
    product: Product = get_product(RedisUnitOfWork(), product_id)
    return product


@router.delete(
    path="/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete(product_id: str):
    delete_product(RedisUnitOfWork(), product_id)
