from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from services.user import create_user, authenticate_user
from database import get_db

router = APIRouter(tags=["auth"])

@router.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return {"message": "User registered", "username": db_user.username}

@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful", "username": db_user.username}

@router.post("/logout/")
def logout():
    return {"message": "Logout successful"}
