from fastapi import FastAPI, Response, HTTPException
import faker
from .cars import create_cars
from typing import List, Dict

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()

@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")

@app.get("/cars", response_model=List[Dict])
def get_cars(page: int = 1, limit: int = 10) -> List[Dict]:
    start = (page - 1) * limit
    end = start + limit
    return cars[start:end]

@app.get("/cars/{id}", response_model=Dict)
def get_car_by_id(id: int):
    car = next((car for car in cars if car["id"] == id), None)
    if car is None:
        raise HTTPException(status_code=404, detail="Машина не найдена")
    return car


