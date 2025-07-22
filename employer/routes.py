from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import JobCreate
from .employer_services import create_job
from employee.employee_services import get_jobs
from database import get_db

router = APIRouter()

@router.post("/jobs/")
def post_job(job: JobCreate, db: Session = Depends(get_db)):
    return create_job(db, job)

@router.get("/jobs/")
def list_jobs(db: Session = Depends(get_db)):
    return get_jobs(db)
