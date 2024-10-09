from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    def create_user(self, db: Session, user: UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(username=user.username, email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

    def update_user(self, db: Session, user_id: int, user: UserCreate):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            for var, value in vars(user).items():
                setattr(db_user, var, value) if value else None
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        return db_user

    def delete_user(self, db: Session, user_id: int):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
        return db_user