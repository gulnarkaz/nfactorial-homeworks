from pydantic import BaseModel

class Car(BaseModel):
    id: int
    name: str
    year: int