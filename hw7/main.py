from fastapi import FastAPI, HTTPException, Depends, status, Form, File, UploadFile, Cookie, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import bcrypt
import jwt
from datetime import datetime, timedelta
import json

app = FastAPI()

SECRET_KEY = "secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    hashed_password: str
    email: str
    photo_data: Optional[bytes] = None

class Flower(BaseModel):
    id: int
    name: str
    cost: float

class Purchase(BaseModel):
    user_id: str
    flower_id: int

class UsersRepository:
    def __init__(self):
        self.users = []
    
    def create_user(self, user: User):
        self.users.append(user)
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        return next((u for u in self.users if u.username == username), None)

class FlowersRepository:
    def __init__(self):
        self.flowers = []
        self.next_id = 1
    
    def add_flower(self, name: str, cost: float) -> int:
        flower = Flower(id=self.next_id, name=name, cost=cost)
        self.flowers.append(flower)
        self.next_id += 1
        return flower.id
    
    def get_all_flowers(self) -> List[Flower]:
        return self.flowers
    
    def get_flowers_by_ids(self, ids: List[int]) -> List[Flower]:
        return [f for f in self.flowers if f.id in ids]

class PurchasesRepository:
    def __init__(self):
        self.purchases = []
    
    def add_purchase(self, user_id: str, flower_id: int):
        self.purchases.append(Purchase(user_id=user_id, flower_id=flower_id))
    
    def get_user_purchases(self, user_id: str) -> List[Purchase]:
        return [p for p in self.purchases if p.user_id == user_id]

users_repo = UsersRepository()
flowers_repo = FlowersRepository()
purchases_repo = PurchasesRepository()

# Auth functions
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        user = users_repo.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# Auth routes
@app.post("/signup")
async def signup(
    username: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    photo: UploadFile = File(None)
):
    if users_repo.get_user_by_username(username):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    photo_data = await photo.read() if photo else None
    
    user = User(
        username=username,
        hashed_password=hashed_password,
        email=email,
        photo_data=photo_data
    )
    users_repo.create_user(user)
    return {"message": "User created"}

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = users_repo.get_user_by_username(username)
    if not user or not bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/profile")
async def profile(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "email": current_user.email,
        "photo": bool(current_user.photo_data)
    }

# Flowers routes
@app.get("/flowers")
async def get_flowers():
    return flowers_repo.get_all_flowers()

@app.post("/flowers")
async def add_flower(name: str = Form(...), cost: float = Form(...)):
    flower_id = flowers_repo.add_flower(name, cost)
    return {"id": flower_id}

# Cart routes
def get_cart_items(cart: str = Cookie(None)) -> List[int]:
    return json.loads(cart) if cart else []

@app.post("/cart/items")
async def add_to_cart(
    flower_id: int = Form(...),
    cart: Optional[str] = Cookie(None)
):
    items = get_cart_items(cart)
    items.append(flower_id)
    response = JSONResponse(content={"message": "Item added"})
    response.set_cookie(key="cart", value=json.dumps(items))
    return response

@app.get("/cart/items")
async def get_cart(cart: str = Cookie(None)):
    items = get_cart_items(cart)
    flowers = flowers_repo.get_flowers_by_ids(items)
    total = sum(f.cost for f in flowers)
    return {
        "items": flowers,
        "total": total
    }

# Purchased routes
@app.post("/purchased")
async def purchase_items(
    current_user: User = Depends(get_current_user),
    cart: str = Cookie(None)
):
    items = get_cart_items(cart)
    for flower_id in items:
        purchases_repo.add_purchase(current_user.username, flower_id)
    
    response = JSONResponse(content={"message": "Purchased successful"})
    response.delete_cookie(key="cart")
    return response

@app.get("/purchased")
async def get_purchased(current_user: User = Depends(get_current_user)):
    purchases = purchases_repo.get_user_purchases(current_user.username)
    flower_ids = [p.flower_id for p in purchases]
    flowers = flowers_repo.get_flowers_by_ids(flower_ids)
    return [{"name": f.name, "cost": f.cost} for f in flowers]