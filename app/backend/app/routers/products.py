from fastapi import APIRouter
from app.services.product_service import get_all_products

router = APIRouter()

@router.get("/products")
def get_products():
    return get_all_products()

