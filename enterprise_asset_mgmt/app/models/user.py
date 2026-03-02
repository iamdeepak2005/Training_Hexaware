from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum
from app.database.base import Base

class UserRole(str, enum.Enum):
    SUPERADMIN = "SUPERADMIN"
    IT_ADMIN = "IT_ADMIN"
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)  # SUPERADMIN, IT_ADMIN, MANAGER, EMPLOYEE
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)

    department = relationship("Department", back_populates="users", foreign_keys=[department_id])
    assignments = relationship("AssetAssignment", back_populates="user")
    requests = relationship("AssetRequest", back_populates="employee", foreign_keys="AssetRequest.employee_id")
    approved_requests = relationship("AssetRequest", back_populates="approver", foreign_keys="AssetRequest.approved_by")
