from sqlalchemy.orm import Session
from app.models.user import User, UserRole
from app.services.leave_service import leave_service
from app.models.leave_request import LeaveStatus

class ManagerController:
    def get_dept_leaves(self, db: Session, current_user: User):
        if not current_user.managed_department:
            return []
        return leave_service.get_department_leaves(db, current_user.managed_department.id)

    def process_leave(self, leave_id: int, status: LeaveStatus, db: Session, current_user: User):
        dept_id = current_user.managed_department.id if current_user.managed_department else None
        return leave_service.approve_reject_leave(
            db, 
            leave_id, 
            status, 
            approver_id=current_user.id, 
            manager_dept_id=dept_id,
            is_admin=(current_user.role == UserRole.ADMIN)
        )

manager_controller = ManagerController()
