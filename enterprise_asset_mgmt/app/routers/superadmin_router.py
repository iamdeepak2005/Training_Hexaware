from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_roles, get_current_user
from app.services.asset_service import AssetService
from app.services.assignment_service import AssignmentService
from app.schemas.asset_schema import AssetCreate, AssetResponse
from app.schemas.user_schema import UserResponse
from app.repositories.user_repo import UserRepo

router = APIRouter(prefix="/superadmin", tags=["superadmin"])

@router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user = Depends(require_roles("SUPERADMIN"))):
    user_repo = UserRepo(db)
    return user_repo.get_all_users()

@router.post("/assets", response_model=AssetResponse)
def create_asset(asset_data: AssetCreate, db: Session = Depends(get_db), current_user = Depends(require_roles("SUPERADMIN"))):
    asset_service = AssetService(db)
    try:
        return asset_service.create_asset(asset_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
