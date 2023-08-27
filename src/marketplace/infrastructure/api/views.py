from __future__ import annotations

from fastapi import APIRouter

from src.marketplace.application.products import get_products_ids
from src.marketplace.infrastructure.adapters.unit_of_work import RedisUnitOfWork


router: APIRouter = APIRouter()


@router.get("/")
async def index() -> dict[str, str]:
    result: list[int] = get_products_ids(RedisUnitOfWork())
    return {"product_ids": result}
