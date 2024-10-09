from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.models.user import User
from app.db.database import get_db
from app.utils.jwt import create_access_token
from app.repositories.user_repository import UserRepository

router = APIRouter()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_repo = UserRepository()
    db_user = db.query(User).filter(
        (User.email == user.login) | (User.username == user.login)
    ).first()
    if not db_user or not db_user.hashed_password == user.password + "notreallyhashed":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
