from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.company_schema import CompanyCreate, CompanyUpdate, CompanyResponse
from app.services.company_service import CompanyService, get_company_service
from app.core.security import get_current_user
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.company_repository import CompanyRepository

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("/", response_model=CompanyResponse)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    repo = CompanyRepository(db)
    return repo.create_company(company, current_user)

@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    repo = CompanyRepository(db)
    company = repo.get_company(company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    if company.owner_user_id != current_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    return company

@router.get("/", response_model=List[CompanyResponse])
def get_companies(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    repo = CompanyRepository(db)
    return repo.get_companies(current_user)

@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    repo = CompanyRepository(db)
    updated_company = repo.update_company(company_id, company, current_user)
    if not updated_company:
        raise HTTPException(status_code=404, detail="Company not found")
    return updated_company

@router.delete("/{company_id}", response_model=CompanyResponse)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    repo = CompanyRepository(db)
    deleted_company = repo.delete_company(company_id, current_user)
    if not deleted_company:
        raise HTTPException(status_code=404, detail="Company not found")
    return deleted_company
