from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.v1.router import api_router

# import models (IMPORTANT)
from app.models import user  # this registers the model

app = FastAPI(title="FinTrack API")
app.include_router(api_router, prefix="/api/v1")
# create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}