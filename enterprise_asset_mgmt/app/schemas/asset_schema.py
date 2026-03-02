from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from enum import Enum

class AssetStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    ASSIGNED = "ASSIGNED"
    MAINTENANCE = "MAINTENANCE"
    RETIRED = "RETIRED"

class AssetBase(BaseModel):
    asset_tag: str
    asset_type: str
    brand: str
    model: str
    purchase_date: date
    status: AssetStatus = AssetStatus.AVAILABLE
    department_id: Optional[int] = None

class AssetCreate(AssetBase):
    pass

class AssetUpdate(BaseModel):
    asset_tag: Optional[str] = None
    asset_type: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    purchase_date: Optional[date] = None
    status: Optional[AssetStatus] = None
    department_id: Optional[int] = None

class AssetResponse(AssetBase):
    id: int

    class Config:
        from_attributes = True
