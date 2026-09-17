from pydantic import BaseModel
from typing import Optional


class AuditCreate(BaseModel):
    project_id: int
    target_url: Optional[str] = None
    description: Optional[str] = None


class AuditResponse(BaseModel):
    id: int
    project_id: int
    status: str
    target_url: Optional[str]
    description: Optional[str]

    class Config:
        from_attributes = True