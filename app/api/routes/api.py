from fastapi import APIRouter

from app.api.routes import health_check, authentication, users, profiles

router = APIRouter()
router.include_router(health_check.router, tags=["Health check"], prefix="/health-check")
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(profiles.router, tags=["profiles"], prefix="/profiles")