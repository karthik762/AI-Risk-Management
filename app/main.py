from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.project import Project
from app.models.audit import Audit

from app.api.projects import router as project_router
from app.api.audits import router as audit_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Risk Manager API",
    version="1.0.0"
)


# Register Project routes
app.include_router(project_router)

# Register Audit routes
app.include_router(audit_router)


@app.get("/")
def root():
    return {
        "message": "AI Risk Manager Backend is running"
    }