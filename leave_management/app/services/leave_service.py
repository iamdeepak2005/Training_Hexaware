from sqlalchemy.orm import Session
from app.repositories.leave_repo import leave_repo
from app.schemas.leave_schema import LeaveCreate
from app.models.leave_request import LeaveStatus
from fastapi import HTTPException
from datetime import date

class LeaveService:
    def apply_leave(self, db: Session, employee_id: int, leave_data: LeaveCreate):
        # Validation: Dates valid
        if leave_data.start_date > leave_data.end_date:
            raise HTTPException(status_code=400, detail="Start date cannot be after end date")
        
        if leave_data.start_date < date.today():
             raise HTTPException(status_code=400, detail="Cannot apply for leave in the past")

        # Validation: No overlapping leave
        overlap = leave_repo.check_overlap(db, employee_id, leave_data.start_date, leave_data.end_date)
        if overlap:
            raise HTTPException(status_code=400, detail="Leave period overlaps with an existing request")

        return leave_repo.create(db, leave_data, employee_id)

    def approve_reject_leave(self, db: Session, leave_id: int, status: LeaveStatus, approver_id: int, manager_dept_id: int = None, is_admin: bool = False):
        leave = leave_repo.get_by_id(db, leave_id)
        if not leave:
            raise HTTPException(status_code=44, detail="Leave request not found")

        if leave.status != LeaveStatus.PENDING and not is_admin:
            raise HTTPException(status_code=400, detail="Only pending requests can be modified by managers")

        # Manager validation: Leave belongs to manager's department
        if not is_admin and manager_dept_id:
            if leave.employee.department_id != manager_dept_id:
                raise HTTPException(status_code=403, detail="Not authorized to approve leave for this department")

        return leave_repo.update_status(db, leave, status, approver_id)

    def get_my_leaves(self, db: Session, employee_id: int):
        return leave_repo.get_employee_leaves(db, employee_id)

    def get_department_leaves(self, db: Session, dept_id: int):
        return leave_repo.get_department_leaves(db, dept_id)

    def get_all_leaves(self, db: Session, skip: int = 0, limit: int = 100):
        return leave_repo.get_all_leaves(db, skip, limit)

leave_service = LeaveService()
