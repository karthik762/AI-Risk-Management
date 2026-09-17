from pydantic import BaseModel
from typing import Optional


class ProjectCreate(BaseModel):
    name: str
    description: str
    github_url: Optional[str] = None


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    github_url: Optional[str]

    class Config:
        from_attributes = True