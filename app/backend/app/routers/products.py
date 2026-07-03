from fastapi import APIRouter
from app.models.product import Product
from app.services.product_service import (
    get_all_products,
    create_product,
    get_product_by_id
)

router = APIRouter()


@router.get("/products")
def get_products():
    return get_all_products()


@router.get("/products/{product_id}")
def get_product(product_id: int):
    return get_product_by_id(product_id)


@router.post("/products")
def add_product(product: Product):
    return create_product(product)