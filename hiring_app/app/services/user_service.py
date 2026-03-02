from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate
from app.exceptions.custom_exceptions import UserNotFoundException, EmailAlreadyRegisteredException

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        user = UserRepository.get_by_id(self.db, user_id)
        if not user:
            raise UserNotFoundException()
        return user

    def list_users(self, skip: int = 0, limit: int = 100):
        return UserRepository.list(self.db, skip, limit)

    def create_user(self, user_data: UserCreate):
        if UserRepository.get_by_email(self.db, user_data.email):
            raise EmailAlreadyRegisteredException()
        
        hashed_password = f"fake_hash_{user_data.password}"
        return UserRepository.create(self.db, user_data, hashed_password)

    def update_user(self, user_id: int, user_data: UserUpdate):
        db_user = self.get_user(user_id)
        return UserRepository.update(self.db, db_user, user_data)

    def delete_user(self, user_id: int):
        db_user = self.get_user(user_id)
        UserRepository.delete(self.db, db_user)
        return {"message": "User deleted successfully"}

def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)
