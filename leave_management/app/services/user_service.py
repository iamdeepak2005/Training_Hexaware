from sqlalchemy.orm import Session
from app.repositories.user_repo import user_repo
from app.schemas.user_schema import UserCreate, UserUpdate
from fastapi import HTTPException

class UserService:
    def create_user(self, db: Session, user: UserCreate):
        existing_user = user_repo.get_by_email(db, user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return user_repo.create(db, user)

    def get_user(self, db: Session, user_id: int):
        user = user_repo.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=44, detail="User not found")
        return user

    def get_all_users(self, db: Session, skip: int = 0, limit: int = 100):
        return user_repo.get_users(db, skip, limit)

user_service = UserService()
