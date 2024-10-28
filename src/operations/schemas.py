from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Union


class GetOperation(BaseModel):
    uid: int


class Operation(BaseModel):
    id: int
    user_id: int
    replenish: int
    total_replenish: int
    total_amount: int
    date: str


class CreateOperation(BaseModel):
    user_id: int
    replenish: int
    total_replenish: int
    total_amount: int
    date: datetime
