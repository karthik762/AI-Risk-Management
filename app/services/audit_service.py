from sqlalchemy.orm import Session

from app.models.audit import Audit
from app.schemas.audit import AuditCreate


def create_audit(
    db: Session,
    audit_data: AuditCreate
):
    audit = Audit(
        project_id=audit_data.project_id,
        target_url=audit_data.target_url,
        description=audit_data.description,
        status="PENDING"
    )

    db.add(audit)
    db.commit()
    db.refresh(audit)

    return audit


def get_audit(
    db: Session,
    audit_id: int
):
    return db.query(Audit).filter(
        Audit.id == audit_id
    ).first()


def get_audits(
    db: Session
):
    return db.query(Audit).all()