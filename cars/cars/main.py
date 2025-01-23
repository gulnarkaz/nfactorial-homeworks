from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List
from .repositories import get_cars_by_name, add_car, get_all_cars
from .models import Car

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"'Cars' - это веб-приложение позволяющее искать, добавлять и отображать список автомобилей"}


@app.get("/cars/search")
def search_cars(request: Request, car_name: str = ""):
    filtered_cars = get_cars_by_name(car_name)
    return templates.TemplateResponse("search.html", {"request": request, "cars": filtered_cars, "car_name": car_name}) 
  
@app.get("/cars/new")
def new_car(request: Request):
    return templates.TemplateResponse("new.html", {"request": request})

@app.get("/cars")
def list_cars(request: Request):
    return templates.TemplateResponse("list.html", {"request": request, "cars": get_all_cars()})

@app.post("/cars/new")
def create_car(name: str = Form(...), year: int = Form(...)):
    add_car(name, year)
    return RedirectResponse(url="/cars", status_code=303)
