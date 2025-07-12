from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.job import apply_to_job
from schemas.job import JobApply
from database import get_db

router = APIRouter()

@router.post("/jobs/apply/")
def apply(job: JobApply, db: Session = Depends(get_db)):
    return apply_to_job(db, job)
