from fastapi import FastAPI
from app.routes import product, category, movement
from app.database import Base, engine

app = FastAPI()

# Create the tables in the database
@app.on_event("startup")
def on_startup():
    print("📦 Creating database tables...")
    Base.metadata.create_all(bind=engine)

app.include_router(product.router)
app.include_router(category.router)
app.include_router(movement.router)

@app.get("/")
def read_root():
    return {"message": "InventoryHub API is running..."}
