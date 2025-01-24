from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.templating import Jinja2Templates

from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/users")
def get_all_users(request: Request):
    return templates.TemplateResponse("users/index.html", {
        "request": request,
        "users": users
        })
    
@app.get("/users/{user_id}")
def get_user(request: Request, response: Response, user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return templates.TemplateResponse("users/user.html", {
        "request": request, 
        "user": user
        })
# Проверим, что пользователь "Robin Monroe" существует
#for user in users:
#    print(user["first_name"], user["last_name"])

