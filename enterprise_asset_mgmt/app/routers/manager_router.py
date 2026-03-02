from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_roles, get_current_user
from app.services.asset_service import AssetService
from app.schemas.asset_schema import AssetResponse
from app.core.pagination import Page

router = APIRouter(prefix="/manager", tags=["manager"])

@router.get("/department/assets", response_model=Page[AssetResponse])
def get_department_assets(page: int = 1, size: int = 20, db: Session = Depends(get_db), current_user = Depends(require_roles("MANAGER", "SUPERADMIN"))):
    asset_service = AssetService(db)
    return asset_service.get_assets(page=page, size=size, department_id=current_user.department_id)
