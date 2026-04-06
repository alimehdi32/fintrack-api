from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.v1.router import api_router
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from app.core.rate_limiter import limiter
from app.models import record, user  # this registers the model
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler
)

app = FastAPI(title="FinTrack API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda r, e: None)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_middleware(SlowAPIMiddleware)
app.include_router(api_router, prefix="/api/v1")

# create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}