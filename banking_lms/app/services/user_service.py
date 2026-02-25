from sqlalchemy.orm import Session
from ..repositories.user_repository import UserRepository
from ..schemas.user_schema import UserCreate, UserUpdate, UserLogin
from fastapi import HTTPException

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user_data: UserCreate):
        if self.repository.get_by_email(user_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.repository.create(user_data)

    def authenticate_user(self, login_data: UserLogin):
        from ..core.security import verify_password
        user = self.repository.get_by_email(login_data.email)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        if not verify_password(login_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid email or password")
            
        return user

    def get_user(self, user_id: int):
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def list_users(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all(skip, limit)

    def update_user(self, user_id: int, user_data: UserUpdate):
        return self.repository.update(user_id, user_data)

    def delete_user(self, user_id: int):
        if not self.repository.delete(user_id):
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
