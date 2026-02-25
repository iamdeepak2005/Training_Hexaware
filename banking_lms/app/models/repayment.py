from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
import enum
from datetime import datetime
from ..core.database import Base

class PaymentStatus(str, enum.Enum):
    COMPLETED = "completed"
    PENDING = "pending"

class Repayment(Base):
    __tablename__ = "repayments"

    id = Column(Integer, primary_key=True, index=True)
    loan_application_id = Column(Integer, ForeignKey("loan_applications.id"), nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.COMPLETED)

    application = relationship("LoanApplication", back_populates="repayments")
