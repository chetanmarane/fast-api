from .models import Job
from sqlalchemy.orm import Session
from .schemas import JobCreate

def create_job(db: Session, job: JobCreate):
    db_job = Job(title=job.title, description=job.description, employer_id=job.employer_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job