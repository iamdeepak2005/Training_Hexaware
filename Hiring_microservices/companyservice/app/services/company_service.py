from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.company_repository import CompanyRepository
from app.schemas.company_schema import CompanyCreate, CompanyUpdate
from app.models.company import Company

class CompanyService:
    def __init__(self, db: Session):
        self.db = db

    def create_company(self, company: CompanyCreate, owner_user_id: str) -> Company:
        repo = CompanyRepository(self.db)
        return repo.create_company(company, owner_user_id)

    def get_company(self, company_id: int) -> Company:
        repo = CompanyRepository(self.db)
        return repo.get_company(company_id)

    def get_companies(self, owner_user_id: str) -> List[Company]:
        repo = CompanyRepository(self.db)
        return repo.get_companies(owner_user_id)

    def update_company(self, company_id: int, company: CompanyUpdate, owner_user_id: str) -> Company:
        repo = CompanyRepository(self.db)
        return repo.update_company(company_id, company, owner_user_id)

    def delete_company(self, company_id: int, owner_user_id: str) -> bool:
        repo = CompanyRepository(self.db)
        return repo.delete_company(company_id, owner_user_id)

# Dependency to get the CompanyService with the DB session
def get_company_service(db: Session = Depends(get_db)):
    return CompanyService(db)