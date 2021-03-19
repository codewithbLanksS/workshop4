from typing import Optional, List
from pydantic import BaseModel, Field


class createRoomsModel(BaseModel):
    id: str = Field(min_length=10, max_length=10)
    rooms_name: str
    price: float


class updateRoomsModel(BaseModel):
    rooms_name: Optional[str]
    price: Optional[float]
