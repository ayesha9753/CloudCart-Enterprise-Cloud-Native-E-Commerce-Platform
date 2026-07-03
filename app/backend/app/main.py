from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.products import router as products_router
app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to CloudCart API"
    }

app.include_router(health_router)
app.include_router(products_router)