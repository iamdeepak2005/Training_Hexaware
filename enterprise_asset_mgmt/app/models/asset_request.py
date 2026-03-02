from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
import enum
from app.database.base import Base

class RequestStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class AssetRequest(Base):
    __tablename__ = "asset_requests"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    asset_type = Column(String)
    reason = Column(Text)
    status = Column(String, default=RequestStatus.PENDING)
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    employee = relationship("User", back_populates="requests", foreign_keys=[employee_id])
    approver = relationship("User", back_populates="approved_requests", foreign_keys=[approved_by])
