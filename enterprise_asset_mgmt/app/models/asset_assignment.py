from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from app.database.base import Base

class AssetAssignment(Base):
    __tablename__ = "asset_assignments"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    assigned_date = Column(Date)
    returned_date = Column(Date, nullable=True)
    condition_on_return = Column(String, nullable=True)

    asset = relationship("Asset", back_populates="assignments")
    user = relationship("User", back_populates="assignments")
