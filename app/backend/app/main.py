from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

# Register SQLAlchemy models
from app.models.product import Product

from app.routers.health import router as health_router
from app.routers.products import router as products_router
from app.models.user import User

app = FastAPI(
    title="CloudCart API",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Welcome to CloudCart API"
    }


app.include_router(health_router)
app.include_router(products_router)