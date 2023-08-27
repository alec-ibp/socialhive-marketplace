from fastapi import APIRouter

from src.marketplace.infrastructure.api.views import router as marketplace_router


router: APIRouter = APIRouter()
router.include_router(marketplace_router, prefix="/marketplace", tags=["marketplace"])
