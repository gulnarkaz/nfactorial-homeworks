from fastapi import APIRouter, Cookie, Depends, HTTPException, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import json
from typing import List, Optional

from app import models, schemas, dependencies
from app.database import get_db

router = APIRouter(prefix="/cart", tags=["cart"])

def get_cart_items(cart: Optional[str] = Cookie(None)) -> List[int]:
    try:
        return json.loads(cart) if cart else []
    except json.JSONDecodeError:
        return []

@router.post("/items")
async def add_to_cart(
    flower_id: int = Form(...),
    cart: Optional[str] = Cookie(None),
    db: Session = Depends(get_db)
):
    # Проверка существования цветка
    flower = db.query(models.Flower).filter(models.Flower.id == flower_id).first()
    if not flower:
        raise HTTPException(status_code=404, detail="Flower not found")
    
    items = get_cart_items(cart)
    items.append(flower_id)
    
    response = JSONResponse(content={"message": "Item added to cart"})
    response.set_cookie(
        key="cart",
        value=json.dumps(items),
        max_age=30*24*60*60,  # 30 дней
        httponly=True
    )
    return response

@router.get("/items", response_model=schemas.CartResponse)
async def get_cart(
    cart: Optional[str] = Cookie(None),
    db: Session = Depends(get_db)
):
    items = get_cart_items(cart)
    
    # Получаем цветы из БД
    flowers = db.query(models.Flower).filter(models.Flower.id.in_(items)).all()
    
    # Сериализация данных
    cart_items = [
        {"id": flower.id, "name": flower.name, "cost": flower.cost}
        for flower in flowers
    ]
    
    total = sum(flower.cost for flower in flowers)
    
    return {
        "items": cart_items,
        "total": round(total, 2)
    }