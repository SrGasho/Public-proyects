from sqlalchemy.orm import Session
from app.models.movement import InventoryMovement
from app.schemas.movement import MovementCreate

def get_movement(db: Session, movement_id: int):
    return db.query(InventoryMovement).filter(InventoryMovement.id == movement_id).first()

def get_movements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InventoryMovement).offset(skip).limit(limit).all()

def create_movement(db: Session, movement: MovementCreate):
    db_movement = InventoryMovement(**movement.model_dump())
    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)
    return db_movement
