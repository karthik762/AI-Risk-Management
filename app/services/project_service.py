from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


def create_project(
    db: Session,
    project_data: ProjectCreate
):
    project = Project(
        name=project_data.name,
        description=project_data.description,
        github_url=project_data.github_url
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_project(
    db: Session,
    project_id: int
):
    return db.query(Project).filter(
        Project.id == project_id
    ).first()


def get_projects(db: Session):
    return db.query(Project).all()