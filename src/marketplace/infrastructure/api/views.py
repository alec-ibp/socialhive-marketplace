from __future__ import annotations

from fastapi import APIRouter

from src.marketplace.domain.models import Product
from src.marketplace.application.products import get_products_ids, add_new_product
from src.marketplace.infrastructure.adapters.unit_of_work import RedisUnitOfWork


router: APIRouter = APIRouter()


@router.get("/products")
async def get_all() -> dict:
    product_ids: list[int] = get_products_ids(RedisUnitOfWork())
    return {"product_ids": product_ids}


@router.post("/products")
async def create(product: Product) -> dict:
    new_product: Product = add_new_product(RedisUnitOfWork(), product)
    return new_product
