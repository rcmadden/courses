from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
# from datetime import date
from database import cars

# get the current year from the date module
# date = date.today()
# current_year = date.year
# print(current_year)

class Car(BaseModel):
    make: str
    model: str
    year: int = Field(...,ge=1970,lt=2023)
    price: float
    engine: Optional[str] = "V4"
    autonomous: bool
    sold: List[str]

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World from FastAPI!'"}


@app.get("/cars", response_model=List[Dict[int, Car]])
def get_cars(number: Optional[str] = Query("10", max_length=3)):
    response = []
    for id, car in list(cars.items())[:int(number)]:
        to_add = {}
        to_add[id] = car
        response.append(to_add)
    return response

