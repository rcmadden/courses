from fastapi import FastAPI, Query, Path, HTTPException, status, Body
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

@app.get("/cars/{id}", response_model=Car)
def get_car(id: int = Path(...,ge=0,lt=1000)):
    car = cars.get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car ID not found")
    return car

@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_cars(body_cars: List[Car], min_id: Optional[int] = Body(0)):
    if len(body_cars) < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No cars to add")
    min_id = len(cars.values()) + min_id
    for car in body_cars:
        while cars.get(min_id):
            min_id += 1
        cars[min_id] = car
        min_id += 1
