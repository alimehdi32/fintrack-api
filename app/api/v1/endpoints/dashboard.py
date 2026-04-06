from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.core.rate_limiter import limiter
from app.services.dashboard_service import get_summary, get_category_breakdown, get_category_by_type
from app.api.deps import get_db, require_roles

router = APIRouter()


@router.get("/summary")
@limiter.limit("5/minute")
def summary(
    request: Request,
    db: Session = Depends(get_db),
    user = Depends(require_roles(["analyst", "admin"]))
):
    return get_summary(db)

@router.get("/categories")
@limiter.limit("5/minute")
def category_breakdown(
    request: Request,
    db: Session = Depends(get_db),
    user = Depends(require_roles(["analyst", "admin"]))
):
    print(f"user: {user}")
    return get_category_breakdown(db)

@router.get("/category-by-type")
@limiter.limit("5/minute")
def category_by_type(
    request: Request,
    db: Session = Depends(get_db),
    user = Depends(require_roles(["analyst", "admin"]))
):
    return get_category_by_type(db)