from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.record import Record
import json
from app.cache.redis_client import redis_client

def get_summary(db: Session):
    cached = redis_client.get("dashboard_summary")

    if cached:
        return json.loads(cached)

    total_income = db.query(func.sum(Record.amount))\
        .filter(Record.type == "income")\
        .scalar() or 0

    total_expense = db.query(func.sum(Record.amount))\
        .filter(Record.type == "expense")\
        .scalar() or 0

    data = {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    }

    redis_client.setex("dashboard_summary", 60, json.dumps(data))

    return data
    
def get_category_breakdown(db):
    results = db.query(
        Record.category,
        func.sum(Record.amount)
    ).group_by(Record.category).all()

    return {category: total for category, total in results}

def get_category_by_type(db):
    results = db.query(
        Record.type,
        Record.category,
        func.sum(Record.amount)
    ).group_by(Record.type, Record.category).all()

    data = {}

    for r_type, category, total in results:
        if r_type not in data:
            data[r_type] = {}
        data[r_type][category] = total

    return data