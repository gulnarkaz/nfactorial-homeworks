from .models import Car

CARS_DB = [
    Car(id=1, name="Toyota Corolla", year=2020),
    Car(id=2, name="Honda Civic", year=2022),
    Car(id=3, name="Ford Mustang", year=2025),
    Car(id=4, name="Chevrolet Camaro", year=1999),
    Car(id=5, name="Tesla Model S", year=2024),
    Car(id=6, name="Toyota Camry", year=2024),
    Car(id=7, name="Honda Accord", year=2024),
    Car(id=7, name="Honda Accord", year=2024),
    Car(id=8, name="BMW", year=2024),
    Car(id=9, name="Volvo", year=2024),
    Car(id=9, name="Kia Rio", year=2024),
    Car(id=10, name="Hyundai Elantra", year=2024),
    Car(id=11, name="Subaru Impreza", year=2024),
    Car(id=12, name="Mazda", year=2024),
    Car(id=13, name="Audi", year=2024),
    Car(id=14, name="Lexus", year=2024),
    Car(id=15, name="Jeep", year=2024),
    Car(id=16, name="Nissan", year=2024),
    Car(id=17, name="Volkswagen", year=2024),
    Car(id=18, name="Mercedes-Benz", year=2024),
    Car(id=19, name="Porsche", year=2024),
    Car(id=20, name="Ferrari", year=2024),
    
]

def get_cars_by_name(car_name: str):
    return [car for car in CARS_DB if car_name.lower() in car.name.lower()]

def add_car(name: str, year: int):
    new_id = len(CARS_DB) + 1
    CARS_DB.append(Car(id=new_id, name=name, year=year))

def get_all_cars():
    return CARS_DB     
