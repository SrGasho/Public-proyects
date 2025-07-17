from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.movement import InventoryMovement, MovementType
from app.schemas.product import ProductCreate, ProductUpdate

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    movement = InventoryMovement(
        product_id=db_product.id,
        product_sku_snapshot=db_product.sku,
        type=MovementType.IN,
        quantity=db_product.quantity,
    )
    db.add(movement)
    db.commit()
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    original_quantity = db_product.quantity

    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    if product.quantity is not None and product.quantity != original_quantity:
        diff = product.quantity - original_quantity
        movement_type = MovementType.IN if diff > 0 else MovementType.OUT

        movement = InventoryMovement(
            product_id=db_product.id,
            product_sku_snapshot=db_product.sku,
            type=movement_type,
            quantity=abs(diff),
        )
        db.add(movement)
        db.commit()

    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    if db_product.quantity > 0:
        movement = InventoryMovement(
            product_id=db_product.id,
            product_sku_snapshot=db_product.sku,
            type=MovementType.OUT,
            quantity=db_product.quantity,
        )
        db.add(movement)
        db.commit()

    db.delete(db_product)
    db.commit()
    return db_product