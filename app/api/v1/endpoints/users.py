from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user
from app.api.deps import get_db

router = APIRouter()


@router.post("/", response_model=UserResponse)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, payload.email, payload.password)