from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
import enum
from ..core.database import Base

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    LOAN_OFFICER = "loan_officer"
    CUSTOMER = "customer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    hashed_password = Column(String, nullable=False)

    applications = relationship("LoanApplication", back_populates="customer", foreign_keys="LoanApplication.user_id")
    processed_applications = relationship("LoanApplication", back_populates="officer", foreign_keys="LoanApplication.processed_by")
