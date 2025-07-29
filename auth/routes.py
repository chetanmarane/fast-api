from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from .token import Token
from sqlalchemy.orm import Session
from user.schemas import UserLogin
from fastapi import Request
from .auth_service import authenticate_user, create_access_token, create_refresh_token, verify_refresh_token
from database import get_db

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)


@auth_router.post('/login', response_model=Token)
async def login_for_access_token(
    user_credentials: UserLogin,
    db: Session = Depends(get_db)
):
    user = authenticate_user(user=user_credentials.username, password=user_credentials.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@auth_router.post("/refresh")
async def refresh_token(request: Request):
    data = await request.json()
    refresh_token = data.get("refresh_token")

    user_email = verify_refresh_token(refresh_token)
    new_access_token = create_access_token(data={"sub": user_email})

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }



# Logout route (stateless JWT: client should delete token)
@auth_router.post('/logout')
async def logout():
    """
    Invalidate the user's token on the client side. For JWT, server cannot truly invalidate unless using a token blacklist.
    """
    return {"message": "Successfully logged out. Please delete your token on the client side."}
