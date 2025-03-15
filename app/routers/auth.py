from fastapi import APIRouter, Depends, HTTPException, status, Form, UploadFile
from app import models, schemas, dependencies
from app.database import get_db
from sqlalchemy.orm import Session
import bcrypt
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the values from the environment
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
async def signup(
    username: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    photo: UploadFile = None,
    db: Session = Depends(get_db)
):
    # Проверка существующего пользователя
    if db.query(models.User).filter(models.User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    photo_data = await photo.read() if photo else None
    
    db_user = models.User(
        username=username,
        hashed_password=hashed_password,
        email=email,
        photo_data=photo_data
    )
    db.add(db_user)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    access_token = jwt.encode(
        {"sub": user.username, "exp": datetime.utcnow() + timedelta(minutes=30)},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile")
async def read_profile(current_user: schemas.User = Depends(dependencies.get_current_user)):
    return current_user