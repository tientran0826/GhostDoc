from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.db.models.document import Document

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("/")
def list_docs(db: Session = Depends(get_db)):
    return db.query(Document).all()
