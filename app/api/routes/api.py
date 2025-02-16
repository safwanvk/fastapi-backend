from fastapi import APIRouter

from app.api.routes import health_check, authentication, users

router = APIRouter()
router.include_router(health_check.router, tags=["Health check"], prefix="/health-check")
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")

"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InN0cmluZyIsImV4cCI6MTc0MDMxNTEzMywic3ViIjoiYWNjZXNzIn0.jW9BLiY3hs_q3hUk-o4OJziwNmAMkI1LUiH-kFEaIwY"