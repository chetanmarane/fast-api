from .models import Job, Application
from sqlalchemy.orm import Session
from .schemas import JobApply
from user.models import User

def get_jobs(db: Session):
    return db.query(Job).all()

def get_employees(db: Session):
    return db.query(User).filter(User.role == "employee").all()

def apply_to_job(db: Session, job_apply: JobApply):
    application = Application(job_id=job_apply.job_id, employee_id=job_apply.employee_id, cover_letter=job_apply.cover_letter)
    db.add(application)
    db.commit()
    db.refresh(application)
    return application