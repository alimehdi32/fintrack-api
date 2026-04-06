from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user
from app.api.deps import get_db, get_current_user, require_roles

router = APIRouter()


@router.post("/", response_model=UserResponse)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, payload.email, payload.password, payload.role)

@router.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user

@router.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user

@router.get("/admin-test")
def admin_test(user = Depends(require_roles(["admin"]))):
    return {"msg": "only admin can see this"}