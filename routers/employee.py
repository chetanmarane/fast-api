from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user import get_employees
from database import get_db

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/employees/")
def list_employees(db: Session = Depends(get_db)):
    return get_employees(db)
