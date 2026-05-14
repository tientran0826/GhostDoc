from datetime import datetime

from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_current_user, get_db
from app.models.document import Document

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("/")
def list_docs(user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    return (
        db.query(Document)
        .filter(Document.user_id == user_id, Document.expires_at > datetime.utcnow())
        .all()
    )


@router.get("/{doc_id}")
def get_doc(
    doc_id: str, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)
):
    doc = (
        db.query(Document)
        .filter(Document.id == doc_id, Document.user_id == user_id)
        .first()
    )

    if not doc:
        return {"error": "not found"}

    return doc


@router.put("/{doc_id}")
def update_doc(
    doc_id: str,
    title: str = Body(None),
    content: str = Body(None),
    expires_at: datetime = Body(None),
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    doc = (
        db.query(Document)
        .filter(Document.id == doc_id, Document.user_id == user_id)
        .first()
    )

    if not doc:
        return {"error": "not found"}

    if title:
        doc.title = title
    if content:
        doc.content = content
    if expires_at:
        doc.expires_at = expires_at

    db.commit()
    db.refresh(doc)

    return doc


@router.delete("/{doc_id}")
def delete_doc(
    doc_id: str, user_id: str = Depends(get_current_user), db: Session = Depends(get_db)
):
    doc = (
        db.query(Document)
        .filter(Document.id == doc_id, Document.user_id == user_id)
        .first()
    )

    if not doc:
        return {"error": "not found"}

    db.delete(doc)
    db.commit()

    return {"message": "deleted"}


@router.post("/")
def create_doc(
    title: str = Body(...),
    content: str = Body(...),
    expires_at: datetime = Body(...),
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    doc = Document(title=title, content=content, user_id=user_id, expires_at=expires_at)

    db.add(doc)
    db.commit()
    db.refresh(doc)

    return doc
