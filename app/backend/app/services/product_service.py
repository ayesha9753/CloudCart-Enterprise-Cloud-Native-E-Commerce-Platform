products = [
    {
        "id": 1,
        "name": "MacBook Pro M4",
        "price": 450000
    },
    {
        "id": 2,
        "name": "Logitech MX Master 3S",
        "price": 32000
    }
]


def get_all_products():
    return products


def create_product(product):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }

    products.append(new_product)
    return new_product

def get_product_by_id(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}

def update_product(product_id: int, updated_product):
    for product in products:
        if product["id"] == product_id:
            product["name"] = updated_product.name
            product["price"] = updated_product.price
            return product

    return {"error": "Product not found"}