from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.dependencies.rbac import require_role
from app.models.user import UserRole
from app.schemas.user_schema import UserResponse, UserCreate
from app.schemas.department_schema import DepartmentResponse, DepartmentCreate
from app.schemas.leave_schema import LeaveResponse
from app.controllers.admin_controller import admin_controller
from app.models.leave_request import LeaveStatus
from app.core.pagination import Page, paginate

router = APIRouter(
    prefix="/admin", 
    tags=["Admin"], 
    dependencies=[Depends(require_role([UserRole.ADMIN]))]
)

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return admin_controller.create_user(user, db)

@router.get("/users", response_model=Page[UserResponse])
def list_users(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * size
    users = admin_controller.list_users(skip, size, db)
    # Mocking total count for now
    return paginate(users, len(users), page, size)

@router.post("/departments", response_model=DepartmentResponse)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
    return admin_controller.create_department(dept, db)

@router.put("/departments/{dept_id}/manager/{manager_id}")
def assign_manager(dept_id: int, manager_id: int, db: Session = Depends(get_db)):
    return admin_controller.assign_manager(dept_id, manager_id, db)

@router.get("/leaves", response_model=Page[LeaveResponse])
def list_all_leaves(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * size
    leaves = admin_controller.list_all_leaves(skip, size, db)
    return paginate(leaves, len(leaves), page, size)

@router.patch("/leaves/{leave_id}/override")
def override_leave(leave_id: int, status: LeaveStatus, db: Session = Depends(get_db)):
    return admin_controller.override_leave(leave_id, status, db)
