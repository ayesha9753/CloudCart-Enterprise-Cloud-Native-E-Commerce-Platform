from fastapi import APIRouter
from app.models.product import Product
from app.services.product_service import (
    get_all_products,
    create_product
)

router = APIRouter()


@router.get("/products")
def get_products():
    return get_all_products()


@router.post("/products")
def add_product(product: Product):
    return create_product(product)