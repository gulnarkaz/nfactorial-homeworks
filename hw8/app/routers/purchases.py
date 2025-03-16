from fastapi import APIRouter, Depends, Cookie, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
import json

from app import models, schemas, dependencies
from app.database import get_db

router = APIRouter(prefix="/purchases", tags=["purchases"])

@router.post("/", response_model=List[schemas.PurchaseResponse])
async def create_purchases(
    current_user: schemas.User = Depends(dependencies.get_current_user),
    cart: str = Cookie(None),
    db: Session = Depends(get_db)
):
    items = json.loads(cart) if cart else []

    if not items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    flowers = db.query(models.Flower).filter(models.Flower.id.in_(items)).all()
    if len(flowers) != len(items):
        raise HTTPException(status_code=404, detail="Some flowers not found")

    purchases = []
    for flower_id in items:
        purchase = models.Purchase(
            user_id=current_user.id,
            flower_id=flower_id
        )
        db.add(purchase)
        purchases.append(purchase)

    db.commit()

    response_data = []
    for purchase in purchases:
        flower = next(f for f in flowers if f.id == purchase.flower_id)
        purchase_response = schemas.PurchaseResponse(
            id=purchase.id,
            user_id=purchase.user_id,
            flower_id=purchase.flower_id,
            flower_name=flower.name,
            flower_cost=flower.cost
        )
        response_data.append(purchase_response)

    response = JSONResponse(content=[p.dict() for p in response_data])
    response.delete_cookie(key="cart")
    return response_data

@router.get("/", response_model=List[schemas.PurchaseResponse])
async def get_purchases(
    current_user: schemas.User = Depends(dependencies.get_current_user),
    db: Session = Depends(get_db)
):
    purchases = db.query(models.Purchase)\
        .join(models.Flower)\
        .filter(models.Purchase.user_id == current_user.id)\
        .with_entities(
            models.Purchase.id,
            models.Purchase.user_id,
            models.Purchase.flower_id,
            models.Flower.name.label("flower_name"),
            models.Flower.cost.label("flower_cost")
        )\
        .all()

    response_data = []
    for p in purchases:
        purchase_response = schemas.PurchaseResponse(
            id=p.id,
            user_id=p.user_id,
            flower_id=p.flower_id,
            flower_name=p.flower_name,
            flower_cost=p.flower_cost
        )
        response_data.append(purchase_response)

    return response_data