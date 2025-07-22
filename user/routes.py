from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserSchema
from .user_services import create_user, authenticate_user, get_users, get_user, delete_user
from database import get_db

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.get('/', response_model=list[UserSchema])
def user_list(db: Session = Depends(get_db)):
    db_users = get_users(db)

    return db_users


# @user_router.get('/me', response_model=UserSchema)
# def user_list(current_user: User = Depends(get_current_active_user)):
#     return current_user



@user_router.get('/{user_id}', response_model=UserSchema)
def user_detail(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@user_router.delete('/{user_id}')
def user_delete(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    delete_user(db, db_user.id)
    return {"message": "User deleted"}

@user_router.post("/register/")
def user_register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return {"message": "User registered", "username": db_user.username}


# @auth_router.post("/login/")
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = authenticate_user(db, user)
#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     return {"message": "Login successful", "username": db_user.username}

# @auth_router.post("/logout/")
# def logout():
#     return {"message": "Logout successful"}