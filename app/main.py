"""
Main FastAPI
"""

from fastapi import FastAPI, HTTPException, Depends
import datetime

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from models.car_models import Car
from models.db_models import Token, User, UserCreate

from utilities.db_connection import create_user, ACCESS_TOKEN_EXPIRE_MINUTES, verify_password, get_db, \
    create_access_token

app = FastAPI()


#####################################

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


#####################################
@app.post("/users/")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


#####################################

cars = []  # Simple in-memory storage


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

