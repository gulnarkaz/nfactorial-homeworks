from fastapi import APIRouter, Depends, HTTPException, status, Form
from app import models, schemas, dependencies
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/flowers", tags=["flowers"])

@router.get("/", response_model=list[schemas.Flower])
def read_flowers(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    flowers = db.query(models.Flower).offset(skip).limit(limit).all()
    return flowers

@router.post("/", response_model=schemas.Flower)
def create_flower(
    name: str = Form(...),
    cost: float = Form(...),
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(dependencies.get_current_user)
):
    db_flower = models.Flower(name=name, cost=cost)
    db.add(db_flower)
    db.commit()
    db.refresh(db_flower)
    return db_flower