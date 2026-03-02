from fastapi import HTTPException,status
from app.repositories.user_repositories import UserRepository
from app.core.security import hash_password,verify_password,create_access_token
from app.models.user import User
from app.schemas.user_schema import RegisterSchema,LoginSchema,TokenSchema

class AuthService:
    def __init__(self,db):
        self.db=db
        self.user_repository=UserRepository(db)

    def register(self,user_data:RegisterSchema):
        user=self.user_repository.get_user_by_email(user_data.email)
        if user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exists")
        user=User(email=user_data.email,role=user_data.role,password=hash_password(user_data.password))
        self.user_repository.create_user(user)
        return user

    def login(self,email:str,password:str):
        user=self.user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
        if not verify_password(password,user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
        access_token=create_access_token(data={"sub":email})
        return {"access_token":access_token,"token_type":"bearer"}
    
    def get_user(self,email:str):
        return self.user_repository.get_user_by_email(email)