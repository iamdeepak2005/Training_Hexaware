from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repo import user_repo
from app.core.security import verify_password, create_access_token
from app.schemas.user_schema import Token

class AuthService:
    def authenticate_user(self, db: Session, email: str, password: str):
        user = user_repo.get_by_email(db, email)
        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user

    def login(self, db: Session, email: str, password: str) -> Token:
        user = self.authenticate_user(db, email, password)
        access_token = create_access_token(
            data={"sub": user.email, "role": user.role.value}
        )
        return Token(access_token=access_token, token_type="bearer")

auth_service = AuthService()
