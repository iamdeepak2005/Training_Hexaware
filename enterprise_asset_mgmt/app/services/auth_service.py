from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepo
from app.core.security import get_password_hash, verify_password, create_access_token
from app.schemas.user_schema import UserCreate, UserResponse

class AuthService:
    def __init__(self, db: Session):
        self.user_repo = UserRepo(db)

    def register_user(self, user_data: UserCreate):
        hashed_password = get_password_hash(user_data.password)
        return self.user_repo.create_user(user_data, hashed_password)

    def login_user(self, email, password):
        user = self.user_repo.get_user_by_email(email)
        if not user or not verify_password(password, user.password):
            return None
        
        access_token = create_access_token(data={"sub": user.email, "role": user.role})
        return {"access_token": access_token, "token_type": "bearer", "user": user}

    def get_current_user_by_email(self, email: str):
        return self.user_repo.get_user_by_email(email)
