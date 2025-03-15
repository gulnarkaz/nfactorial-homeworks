from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    photo_data: Optional[bytes] = None
    is_active: bool = True
    
    model_config = {"from_attributes": True}



class FlowerBase(BaseModel):
    name: str
    cost: float

class FlowerCreate(FlowerBase):
    id: Optional[int] = None


class Flower(FlowerBase):
    id: int
    
    model_config = {"from_attributes": True}



class CartItem(BaseModel):
    id: int
    name: str
    cost: float

class CartResponse(BaseModel):
    items: List[CartItem]
    total: float


# Purchase Schemas
class PurchaseBase(BaseModel):
    user_id: int
    flower_id: int

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int
    
    
    model_config = {"from_attributes": True}


class PurchaseResponse(Purchase):
    flower_name: str
    flower_cost: float

class PurchaseDetail(Purchase):
    flower: Flower

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None