from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.core.rate_limiter import limiter
from app.schemas.record import RecordCreate, RecordResponse
from app.services.record_service import create_record, get_records
from app.api.deps import get_db, require_roles

router = APIRouter()


@router.post("/", response_model=RecordResponse)
@limiter.limit("5/minute")
def add_record(
    request: Request,
    payload: RecordCreate,
    db: Session = Depends(get_db),
    user = Depends(require_roles(["admin"]))
):
    return create_record(db, payload)


@router.get("/", response_model=list[RecordResponse])
@limiter.limit("5/minute")
def list_records(
    request: Request,
    db: Session = Depends(get_db),
    user = Depends(require_roles(["analyst", "admin"]))
):
    return get_records(db)