from sqlalchemy.orm import Session

from app.repositories.product_repository import (
    get_all_products as repo_get_all_products,
    get_product_by_id as repo_get_product_by_id,
    create_product as repo_create_product,
    update_product as repo_update_product,
    delete_product as repo_delete_product,
)


def get_all_products(db: Session):
    return repo_get_all_products(db)


def get_product_by_id(db: Session, product_id: int):
    return repo_get_product_by_id(db, product_id)


def create_product(db: Session, product):
    return repo_create_product(
        db=db,
        name=product.name,
        price=product.price,
    )


def update_product(db: Session, product_id: int, product):
    return repo_update_product(
        db=db,
        product_id=product_id,
        name=product.name,
        price=product.price,
    )


def delete_product(db: Session, product_id: int):
    return repo_delete_product(db, product_id)