from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.dependencies.rbac import get_current_user
from app.models.user import User
from app.schemas.leave_schema import LeaveResponse, LeaveCreate
from app.controllers.employee_controller import employee_controller

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.post("/leaves", response_model=LeaveResponse)
def apply_leave(leave: LeaveCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return employee_controller.apply_leave(leave, db, current_user.id)

@router.get("/leaves", response_model=List[LeaveResponse])
def get_my_leaves(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return employee_controller.get_my_leaves(db, current_user.id)
