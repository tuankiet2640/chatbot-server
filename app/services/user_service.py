from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, User
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db: Session, user: UserCreate):
        return self.user_repository.create_user(db, user)

    def get_user(self, db: Session, user_id: int):
        return self.user_repository.get_user(db, user_id)

    def get_user_by_email(self, db: Session, email: str):
        return self.user_repository.get_user_by_email(db, email)

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return self.user_repository.get_users(db, skip, limit)

    def update_user(self, db: Session, user_id: int, user: UserCreate):
        return self.user_repository.update_user(db, user_id, user)

    def delete_user(self, db: Session, user_id: int):
        return self.user_repository.delete_user(db, user_id)