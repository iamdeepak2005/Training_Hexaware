from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from app.database.base import Base

class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.EMPLOYEE)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)

    # Relationship to Department (as an employee)
    department = relationship("Department", back_populates="employees", foreign_keys=[department_id])
    
    # Relationship to Department (as a manager)
    managed_department = relationship("Department", back_populates="manager", uselist=False, foreign_keys="Department.manager_id")
    
    # Relationship to Leave Requests
    leave_requests = relationship("LeaveRequest", back_populates="employee", foreign_keys="LeaveRequest.employee_id")
    approved_leaves = relationship("LeaveRequest", back_populates="approver", foreign_keys="LeaveRequest.approved_by")
