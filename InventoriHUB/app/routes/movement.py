from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.movement import MovementCreate, MovementOut
from app.crud import movement as crud_movement
from app.database import get_db
from typing import List

router = APIRouter(prefix="/movements", tags=["Movements"])

@router.post("/", response_model=MovementOut)
def create_movement(movement: MovementCreate, db: Session = Depends(get_db)):
    try:
        return crud_movement.create_movement(db, movement)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[MovementOut])
def get_movements(db: Session = Depends(get_db)):
    return crud_movement.get_movements(db)
