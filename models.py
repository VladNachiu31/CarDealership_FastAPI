"""
Models FastApi
"""

from pydantic import BaseModel

class Car(BaseModel):
    make: str
    model: str
    year: int
    price: float

