from sqlalchemy.orm import Session
from app import models, schemas

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db:Session):
    return db.query(models.Item).all()

def get_item(db:Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id== item_id).first()