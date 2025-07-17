from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum as SqlEnum, String, func
from app.database import Base
from enum import Enum
from sqlalchemy.orm import relationship

class MovementType(str, Enum):
    IN = "in"
    OUT = "out"

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="SET NULL"), nullable=True)
    product_sku_snapshot = Column(String(100), nullable=True)
    type = Column(SqlEnum(MovementType), nullable=False)
    quantity = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    product = relationship("Product", back_populates="movements")
