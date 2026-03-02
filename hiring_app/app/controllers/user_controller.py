from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService, get_user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user_data)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)

@router.get("/", response_model=List[UserResponse])
def list_users(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1), 
    service: UserService = Depends(get_user_service)
):
    return service.list_users(skip, limit)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, service: UserService = Depends(get_user_service)):
    return service.update_user(user_id, user_data)

@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.delete_user(user_id)
