from fastapi import APIRouter

from app.api.routes import health_check

router = APIRouter()
router.include_router(health_check.router, tags=["Health check"], prefix="/health-check")