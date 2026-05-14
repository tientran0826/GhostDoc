from fastapi import FastAPI

from app.api.router import api_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="GhostDoc API")

app.include_router(api_router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("DB ready")
