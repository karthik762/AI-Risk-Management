from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.audit import AuditCreate, AuditResponse
from app.services.audit_service import (
    create_audit,
    get_audit,
    get_audits
)


router = APIRouter(
    prefix="/api/audits",
    tags=["Audits"]
)


@router.post(
    "",
    response_model=AuditResponse
)
def create(
    audit: AuditCreate,
    db: Session = Depends(get_db)
):
    return create_audit(db, audit)


@router.get(
    "",
    response_model=list[AuditResponse]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_audits(db)


@router.get(
    "/{audit_id}",
    response_model=AuditResponse
)
def get_one(
    audit_id: int,
    db: Session = Depends(get_db)
):
    audit = get_audit(db, audit_id)

    if not audit:
        raise HTTPException(
            status_code=404,
            detail="Audit not found"
        )

    return audit