from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.dependencies.rbac import require_role, get_current_user
from app.models.user import UserRole, User
from app.schemas.leave_schema import LeaveResponse
from app.controllers.manager_controller import manager_controller
from app.models.leave_request import LeaveStatus

router = APIRouter(
    prefix="/manager", 
    tags=["Manager"], 
    dependencies=[Depends(require_role([UserRole.MANAGER, UserRole.ADMIN]))]
)

@router.get("/department/leaves", response_model=List[LeaveResponse])
def get_dept_leaves(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return manager_controller.get_dept_leaves(db, current_user)

@router.patch("/leaves/{leave_id}/process")
def process_leave(leave_id: int, status: LeaveStatus, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return manager_controller.process_leave(leave_id, status, db, current_user)
