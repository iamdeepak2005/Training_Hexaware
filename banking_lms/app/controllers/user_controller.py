from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..schemas.user_schema import UserCreate, UserUpdate, UserOut, UserLogin
from ..services.user_service import UserService
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)

@router.post("/login", response_model=UserOut)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.authenticate_user(login_data)

@router.get("/{id}", response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user(id)

@router.get("/", response_model=List[UserOut])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.list_users(skip, limit)

@router.put("/{id}", response_model=UserOut)
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user(id, user)

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.delete_user(id)
