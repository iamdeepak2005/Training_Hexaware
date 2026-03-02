from sqlalchemy.orm import Session
from app.schemas.leave_schema import LeaveCreate
from app.services.leave_service import leave_service

class EmployeeController:
    def apply_leave(self, leave: LeaveCreate, db: Session, employee_id: int):
        return leave_service.apply_leave(db, employee_id, leave)

    def get_my_leaves(self, db: Session, employee_id: int):
        return leave_service.get_my_leaves(db, employee_id)

employee_controller = EmployeeController()
