from models.models import Job, Application
from sqlalchemy.orm import Session
from schemas.job import JobCreate, JobApply

def create_job(db: Session, job: JobCreate):
    db_job = Job(title=job.title, description=job.description, employer_id=job.employer_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db: Session):
    return db.query(Job).all()

def apply_to_job(db: Session, job_apply: JobApply):
    application = Application(job_id=job_apply.job_id, employee_id=job_apply.employee_id, cover_letter=job_apply.cover_letter)
    db.add(application)
    db.commit()
    db.refresh(application)
    return application
