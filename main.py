from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import (
    auth,
    flowers,
    cart,
    purchases
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router)
app.include_router(flowers.router)
app.include_router(cart.router)
app.include_router(purchases.router)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to Flower Shop API!"
    }