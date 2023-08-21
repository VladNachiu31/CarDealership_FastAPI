"""
Main FastApi
"""

from fastapi import FastAPI

from models import Car

app = FastAPI()
cars = [] # Simple in-memory storage

@app.post("/api/cars/")
async def create_car(car: Car):
    cars.append(car.dict())
    return car

@app.get("/api/cars/")
async def get_cars():
    return cars

@app.get("/api/cars/{car_id}")
async def get_car(car_id: int):
    return cars[car_id]

@app.put("/api/cars/{car_id}")
async def update_car(car_id: int, car: Car):
    cars[car_id] = car.dict()
    return car

@app.delete("/api/cars/{car_id}")
async def delete_car(car_id: int):
    return cars.pop(car_id)

