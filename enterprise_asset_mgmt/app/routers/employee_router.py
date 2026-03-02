from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import require_roles, get_current_user
from app.services.request_service import RequestService
from app.services.assignment_service import AssignmentService
from app.schemas.request_schema import RequestCreate, RequestResponse
from app.schemas.assignment_schema import AssignmentResponse

router = APIRouter(prefix="/employee", tags=["employee"])

@router.post("/requests", response_model=RequestResponse)
def create_request(req_data: RequestCreate, db: Session = Depends(get_db), current_user = Depends(require_roles("EMPLOYEE", "MANAGER", "IT_ADMIN", "SUPERADMIN"))):
    request_service = RequestService(db)
    return request_service.create_request(req_data, employee_id=current_user.id)

@router.get("/assets", response_model=List[AssignmentResponse])
def get_own_assets(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    assignment_service = AssignmentService(db)
    return assignment_service.get_user_assignments(user_id=current_user.id)
