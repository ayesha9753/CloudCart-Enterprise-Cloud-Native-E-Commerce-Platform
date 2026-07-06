from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)


def register_user(db: Session, user):
    existing = get_user_by_email(db, user.email)

    if existing:
        return None

    hashed_password = hash_password(user.password)

    return create_user(
        db=db,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )


def login_user(db: Session, user):
    existing = get_user_by_email(db, user.email)

    if existing is None:
        return None

    if not verify_password(
        user.password,
        existing.hashed_password,
    ):
        return None

    access_token = create_access_token(
        {
            "sub": existing.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }