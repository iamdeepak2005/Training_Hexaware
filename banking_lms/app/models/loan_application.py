from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from ..core.database import Base

class LoanStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    DISBURSED = "disbursed"
    CLOSED = "closed"

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("loan_products.id"), nullable=False)
    requested_amount = Column(Float, nullable=False)
    approved_amount = Column(Float)
    status = Column(Enum(LoanStatus), default=LoanStatus.PENDING)
    processed_by = Column(Integer, ForeignKey("users.id"))

    customer = relationship("User", back_populates="applications", foreign_keys=[user_id])
    officer = relationship("User", back_populates="processed_applications", foreign_keys=[processed_by])
    product = relationship("LoanProduct", back_populates="applications")
    repayments = relationship("Repayment", back_populates="application")
