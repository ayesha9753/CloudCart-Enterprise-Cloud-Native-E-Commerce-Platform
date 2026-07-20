from prometheus_fastapi_instrumentator import Instrumentator
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database.base import Base
from app.database.database import engine

from app.models.product import Product
from app.models.user import User

from app.routers.auth import router as auth_router
from app.routers.health import router as health_router
from app.routers.products import router as products_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="CloudCart API",
    version="1.0.0",
    lifespan=lifespan,
)

# 👇 Ye line yahan honi chahiye
Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {"message": "Welcome to CloudCart API"}


app.include_router(health_router)
app.include_router(products_router)
app.include_router(auth_router)