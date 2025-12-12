from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models

item_router = APIRouter(prefix="/items")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@item_router.post("/")
def add_item(name: str, db: Session = Depends(get_db)):
    new_item = models.Item(name=name)
    db.add(new_item)
    db.commit()
    return {"status": "success", "item": name}

@item_router.get("/")
def list_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items
