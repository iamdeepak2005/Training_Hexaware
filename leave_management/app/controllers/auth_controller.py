from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth_service import auth_service
from app.schemas.user_schema import Token, UserCreate, UserResponse
from app.services.user_service import user_service

class AuthController:
    def login(self, form_data: OAuth2PasswordRequestForm, db: Session):
        return auth_service.login(db, form_data.username, form_data.password)

    def register(self, user: UserCreate, db: Session):
        return user_service.create_user(db, user)

auth_controller = AuthController()
