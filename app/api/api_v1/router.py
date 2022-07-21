from fastapi import APIRouter
from app.api.api_v1.handlers.user import user_router
from app.api.auth.jwt import auth_router
from app.api.api_v1.handlers.product import product_router
from app.api.api_v1.handlers.basket import basket_router


router = APIRouter()
router.include_router(router=user_router, prefix='/users',tags=["users"])
router.include_router(router=auth_router, prefix='/auth',tags=["auth"])
router.include_router(router=product_router, prefix='/product',tags=["product"])
router.include_router(router=basket_router, prefix='/basket',tags=["basket"])
