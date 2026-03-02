from fastapi import APIRouter,Depends
from app.services.auth_service import AuthService
from app.database.session import get_db
from sqlalchemy.orm import Session
from app.schemas.user_schema import RegisterSchema

router=APIRouter(prefix="/auth",tags=["Authentication"])

def get_auth_service(db:Session=Depends(get_db)):
    return AuthService(db)

@router.post("/register")
def register(user_data:RegisterSchema,auth_service=Depends(get_auth_service)):
    user= auth_service.register(user_data)
    return {"message":"User registered successfully","id":user.id}

@router.post("/login")
def login(email:str,password:str,auth_service=Depends(get_auth_service)):
    user= auth_service.login(email,password)
    return {"message":"User logged in successfully","user":user}

