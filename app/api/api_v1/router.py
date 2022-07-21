from fastapi import APIRouter
from app.api.api_v1.handlers.user import user_router
from app.api.auth.jwt import auth_router
router = APIRouter()

router.include_router(router=user_router, prefix='/users',tags=["users"])
router.include_router(router=auth_router, prefix='/auth',tags=["auth"])