from fastapi import APIRouter

from app.api.routes import health, recipes

router = APIRouter()
router.include_router(health.router, prefix="/health", tags=["health"])
router.include_router(recipes.router, prefix="/recipes", tags=["health"])
