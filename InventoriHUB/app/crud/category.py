from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate
from app.schemas.category import CategoryCreate, CategoryUpdate

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category: CategoryUpdate):
    db_category = get_category(db, category_id)
    if not db_category:
        return None

    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    if db_category.products:
        return "has_products"
    db.delete(db_category)
    db.commit()
    return db_category

