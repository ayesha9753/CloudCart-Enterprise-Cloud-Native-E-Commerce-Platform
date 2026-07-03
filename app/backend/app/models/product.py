from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: int
from app.services.product_service import (
    delete_product,
    get_all_products,
    create_product,
    get_product_by_id
)
import update_product
@router.put("/products/{product_id}")
def update_existing_product(product_id: int, product: Product):
    return update_product(product_id, product)

import delete_product
@router.delete("/products/{product_id}")
def remove_product(product_id: int):
    return delete_product(product_id)