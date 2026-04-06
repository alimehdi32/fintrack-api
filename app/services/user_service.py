from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password
from fastapi import HTTPException

def create_user(db: Session, email: str, password: str, role: str = "viewer"):
    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    if role not in ["viewer", "analyst", "admin"]:
        raise HTTPException(status_code=400, detail="Invalid role")

    hashed_password = hash_password(password)

    user = User(
        email=email,
        password_hash=hashed_password,
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user