from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.schemas.department_schema import DepartmentCreate
from app.services.user_service import user_service
from app.services.department_service import department_service
from app.services.leave_service import leave_service
from app.models.leave_request import LeaveStatus
from app.core.pagination import paginate

class AdminController:
    def create_user(self, user: UserCreate, db: Session):
        return user_service.create_user(db, user)

    def list_users(self, skip: int, limit: int, db: Session):
        users = user_service.get_all_users(db, skip, limit)
        # For simplicity, we assume total is len if we don't have a count repo method
        # but let's just return the list for now or wrap it if router expectations change.
        return users

    def create_department(self, dept: DepartmentCreate, db: Session):
        return department_service.create_department(db, dept)

    def assign_manager(self, dept_id: int, manager_id: int, db: Session):
        return department_service.assign_manager(db, dept_id, manager_id)

    def list_all_leaves(self, skip: int, limit: int, db: Session):
        return leave_service.get_all_leaves(db, skip, limit)

    def override_leave(self, leave_id: int, status: LeaveStatus, db: Session):
        return leave_service.approve_reject_leave(db, leave_id, status, approver_id=0, is_admin=True)

admin_controller = AdminController()
