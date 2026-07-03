from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: int
from app.services.product_service import (
    get_all_products,
    create_product,
    get_product_by_id
)