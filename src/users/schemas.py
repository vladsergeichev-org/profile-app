from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Union


class TypeSearch(Enum):
    uid = "uid"
    email = "email"
    username = "username"


class UserSearch(BaseModel):
    type: Union[TypeSearch]
    value: Union[str, int]


class UserCreate(BaseModel):
    name: str
    surname: str
    username: str
    password: str
    email: str


class UserLogin(BaseModel):
    username: str
    password: str
