from fastapi import APIRouter

from app.api import auth, documents

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(documents.router)
