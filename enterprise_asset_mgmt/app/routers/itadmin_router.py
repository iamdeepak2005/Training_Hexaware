from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_roles, get_current_user
from app.services.asset_service import AssetService
from app.services.assignment_service import AssignmentService
from app.services.request_service import RequestService
from app.schemas.asset_schema import AssetCreate, AssetResponse
from app.schemas.assignment_schema import AssignmentCreate, AssignmentResponse, AssignmentReturn
from app.schemas.request_schema import RequestResponse
from app.core.pagination import Page

router = APIRouter(prefix="/itadmin", tags=["itadmin"])

@router.post("/assets", response_model=AssetResponse)
def create_asset(asset_data: AssetCreate, db: Session = Depends(get_db), current_user = Depends(require_roles("IT_ADMIN", "SUPERADMIN"))):
    asset_service = AssetService(db)
    try:
        return asset_service.create_asset(asset_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/assets", response_model=Page[AssetResponse])
def get_assets(page: int = 1, size: int = 20, status: str = None, dep_id: int = None, db: Session = Depends(get_db), current_user = Depends(require_roles("IT_ADMIN", "SUPERADMIN"))):
    asset_service = AssetService(db)
    return asset_service.get_assets(page=page, size=size, status=status, department_id=dep_id)

@router.post("/assignments", response_model=AssignmentResponse)
def assign_asset(assign_data: AssignmentCreate, db: Session = Depends(get_db), current_user = Depends(require_roles("IT_ADMIN", "SUPERADMIN"))):
    assignment_service = AssignmentService(db)
    try:
        return assignment_service.assign_asset(assign_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/assets/{asset_id}/return", response_model=AssignmentResponse)
def return_asset(asset_id: int, return_data: AssignmentReturn, db: Session = Depends(get_db), current_user = Depends(require_roles("IT_ADMIN", "SUPERADMIN"))):
    assignment_service = AssignmentService(db)
    try:
        return assignment_service.return_asset(asset_id, return_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/requests/{req_id}/approve", response_model=RequestResponse)
def approve_request(req_id: int, db: Session = Depends(get_db), it_admin = Depends(require_roles("IT_ADMIN", "SUPERADMIN"))):
    request_service = RequestService(db)
    return request_service.approve_request(req_id, it_admin.id)

@router.post("/requests/{req_id}/reject", response_model=RequestResponse)
def reject_request(req_id: int, db: Session = Depends(get_db), it_admin = Depends(require_roles("IT_ADMIN", "SUPERADMIN"))):
    request_service = RequestService(db)
    return request_service.reject_request(req_id, it_admin.id)
