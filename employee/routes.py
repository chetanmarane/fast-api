from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .employee_services import get_employees, apply_to_job
from database import get_db
from .schemas import JobApply

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/employees/")
def list_employees(db: Session = Depends(get_db)):
    return get_employees(db)


@router.post("/jobs/apply/")
def apply(job: JobApply, db: Session = Depends(get_db)):
    return apply_to_job(db, job)
