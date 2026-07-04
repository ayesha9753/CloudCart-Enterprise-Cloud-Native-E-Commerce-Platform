from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres@db:5432/cloudcart"

engine = create_engine(
    DATABASE_URL,
    echo=True
)