from sqlalchemy.orm import Session
from app.models.leave_request import LeaveRequest, LeaveStatus
from app.schemas.leave_schema import LeaveCreate
from datetime import date

class LeaveRepository:
    def get_by_id(self, db: Session, leave_id: int):
        return db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

    def create(self, db: Session, leave: LeaveCreate, employee_id: int):
        db_leave = LeaveRequest(
            **leave.model_dump(),
            employee_id=employee_id,
            status=LeaveStatus.PENDING
        )
        db.add(db_leave)
        db.commit()
        db.refresh(db_leave)
        return db_leave

    def get_employee_leaves(self, db: Session, employee_id: int):
        return db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id).all()

    def get_department_leaves(self, db: Session, department_id: int):
        from app.models.user import User
        return db.query(LeaveRequest).join(User, LeaveRequest.employee_id == User.id)\
                 .filter(User.department_id == department_id).all()

    def get_all_leaves(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(LeaveRequest).offset(skip).limit(limit).all()

    def update_status(self, db: Session, db_leave: LeaveRequest, status: LeaveStatus, approver_id: int):
        db_leave.status = status
        db_leave.approved_by = approver_id
        db.commit()
        db.refresh(db_leave)
        return db_leave

    def check_overlap(self, db: Session, employee_id: int, start_date: date, end_date: date):
        return db.query(LeaveRequest).filter(
            LeaveRequest.employee_id == employee_id,
            LeaveRequest.status != LeaveStatus.REJECTED,
            LeaveRequest.start_date <= end_date,
            LeaveRequest.end_date >= start_date
        ).first()

leave_repo = LeaveRepository()
