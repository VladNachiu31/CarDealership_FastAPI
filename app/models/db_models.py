"""
Car models FastAPI
"""

from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    username: str
    password: str
