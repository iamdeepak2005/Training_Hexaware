from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
import enum
from datetime import datetime
from app.database.base import Base

class AssetStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    ASSIGNED = "ASSIGNED"
    MAINTENANCE = "MAINTENANCE"
    RETIRED = "RETIRED"

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_tag = Column(String, unique=True, index=True)
    asset_type = Column(String)  # Laptop, Monitor, License, etc.
    brand = Column(String)
    model = Column(String)
    purchase_date = Column(Date)
    status = Column(String, default=AssetStatus.AVAILABLE)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)

    department = relationship("Department", back_populates="assets")
    assignments = relationship("AssetAssignment", back_populates="asset")
