from sqlalchemy.orm import Session

from app.models.product import Product


def get_all_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, name: str, price: int):
    product = Product(name=name, price=price)

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def update_product(db: Session, product_id: int, name: str, price: int):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    product.name = name
    product.price = price

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    if not product:
        return False

    db.delete(product)
    db.commit()

    return True