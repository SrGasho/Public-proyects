from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class MovementType(str, Enum):
    IN = "in"
    OUT = "out"

class MovementBase(BaseModel):
    product_id: int | None
    product_sku_snapshot: str | None
    type: MovementType
    quantity: int

class MovementCreate(MovementBase):
    pass

class MovementOut(MovementBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
