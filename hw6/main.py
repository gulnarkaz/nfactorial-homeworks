from fastapi import FastAPI, templating, Request, Form, Response, Cookie
from fastapi.responses import RedirectResponse
from attrs import define
from jose import jwt
import json
@define
class User:
    id: int = None  
    email: str = ""  
    name: str = ""
    login: str = ""
    password: str = ""
  
class UsersRepository:
    def __init__(self):
        self.users = []
    
    def save(self, user: User):
        user.id = len(self.users) + 1
        self.users.append(user)
        
    def get_by_login(self, login: str) -> User: 
        for user in self.users:
            if user.login == login:
                return user
        return None
    def get_by_id(self, id: int) -> User: 
        for user in self.users:
            if user.id == id:
                return user
        return None     
    
@define 
class Flower:
    id: int = None
    name: str = ""
    amount: int = 0
    price: int = 0
    
class FlowersRepository:
    def __init__(self):
        self.flowers = []
    
    def save(self, flower: Flower):
        flower.id = len(self.flowers) + 1
        self.flowers.append(flower)
        
    def get_all_flowers(self):
        return self.flowers
    
    def get_flower_by_id(self, flower_id: int) -> Flower:
        for flower in self.flowers:
            if flower.id == flower_id:
                return flower 
        return None
@define 
class Purchase:
    user_id: int
    flower_id: int 
    
class PurchasesRepository:
    def __init__(self):
        self.purchases = []
        
    def add_purchase(self, user_id, flower_id):
        self.purchases.append(Purchase(user_id, flower_id))
        
    def get_purchases_by_user(self, user_id: int):
        return [p for p in self.purchases if p.user_id == user_id]
        

app = FastAPI()   
templates = templating.Jinja2Templates("templates")
users_repo = UsersRepository()
flowers_repo = FlowersRepository()
purchase_repo = PurchasesRepository()

def create_jwt(user_id: int) -> str:
    body = {"user_id": user_id}
    token = jwt.encode(body, "user-secret", "HS256")
    return token

def decode_jwt(token: str) -> int:
    data = jwt.decode(token, "user-secret", "HS256")
    return data["user_id"]
                    
@app.get("/signup")
def get_signup(request: Request):
    return templates.TemplateResponse("users/signup.html", {
        "request": request
    })

@app.post("/signup")
def post_signup(
    request: Request,
    email: str = Form(),
    name: str = Form(),
    login: str = Form(),
    password: str = Form()
):
    user = User(email=email, name=name, login=login, password=password)
    users_repo.save(user)
    return RedirectResponse("/login", status_code=303)

@app.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("users/login.html", {
        "request": request
    })
    
@app.post("/login")
def post_login(
    request: Request,
    response: Response,
    login: str = Form(),
    password: str = Form()
):
    user = users_repo.get_by_login(login)
    if user is None or user.password != password:
        return Response("Permission denied!")
        
    response = RedirectResponse("/profile", status_code=303)
    token = create_jwt(user.id)
    response.set_cookie("token", token)
    return response 
    

@app.get("/profile")
def get_profile(
    request: Request,
    token: str = Cookie(),            
):
    user_id = decode_jwt(token)
        
    return templates.TemplateResponse(
        "users/profile.html", 
        {
        "request": request,
        "user": users_repo.get_by_id(user_id)
        }
    )
    
@app.get("/flowers")
def get_flowers(request: Request):
    return templates.TemplateResponse(
        "flowers/newflower.html", 
        {
        "request": request, 
        "flowers": flowers_repo.get_all_flowers()
        }
    )
    
@app.post("/flowers")
def post_flowers(
    request: Request,
    name: str = Form(),
    amount: int = Form(),
    price: int = Form(),
    
):
    flower = Flower(name=name, amount=amount, price=price)
    flowers_repo.save(flower)
    return RedirectResponse("/flowers", status_code=303)
@app.get("/cart/items")
def get_cart(
    request: Request,
    token: str = Cookie(),
):
    user_id = decode_jwt(token)
    cart = request.cookies.get("cart", "[]")
    cart = json.loads(cart)
    flowers = []
    total_price = 0
    for flower_id in cart:
        flower = flowers_repo.get_flower_by_id(flower_id)
        if flower is not None:
            flowers.append(flower)
            total_price += flower.price
    return templates.TemplateResponse(
        "flowers/cart_items.html",
        {
            "request": request,
            "flowers": flowers,
            "total_price": total_price
        }
    )
    
@app.post("/cart/items")
def add_to_cart(
    request: Request,
    flower_id: int = Form(),
    token: str = Cookie(),
    
):
    user_id = decode_jwt(token)
    cart_cookie = request.cookies.get("cart")
    cart = json.loads(cart_cookie) if cart_cookie else []
    
    if flower_id not in cart:
        cart.append(flower_id)
    
    response = RedirectResponse("/flowers", status_code=303)
    response.set_cookie("cart", json.dumps(cart))
    return response


@app.post("/purchased")
def purchase_items(
    request: Request,
    response: Response,
    token: str = Cookie()
):
    user_id = decode_jwt(token)

    cart = json.loads(request.cookies.get("cart"))

    for flower_id in cart:
        purchase_repo.add_purchase(user_id, flower_id)
    
    response = RedirectResponse("/purchased", status_code=303)
    return response

@app.get("/purchased")
def get_purchased(
    request: Request,
    token: str = Cookie()
):  
    user_id = decode_jwt(token)
    
    purchases = purchase_repo.get_purchases_by_user(user_id)

    flowers = []
    for purchase in purchases:
        flower = flowers_repo.get_flower_by_id(purchase.flower_id)
        if flower is not None:
            flowers.append(flower)
    
    return templates.TemplateResponse(
        "flowers/purchased_items.html", 
        {
            "request": request,
            "flowers": flowers
        }
    )