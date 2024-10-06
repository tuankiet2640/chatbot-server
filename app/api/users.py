from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, User
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db.database import get_db

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository())

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db), service: UserService = Depends(get_user_service)):
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db=db, user=user)

@router.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), service: UserService = Depends(get_user_service)):
    users = service.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db), service: UserService = Depends(get_user_service)):
    db_user = service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db), service: UserService = Depends(get_user_service)):
    db_user = service.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db), service: UserService = Depends(get_user_service)):
    db_user = service.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user