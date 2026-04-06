from sqlalchemy.orm import Session
from app.models.record import Record
from app.cache.redis_client import redis_client
from fastapi import HTTPException

def create_record(db: Session, data):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    record = Record(**data.dict())

    db.add(record)
    db.commit()
    db.refresh(record)

    return record

def get_records(db: Session):
    return db.query(Record).all()