from typing import List
from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company_schema import CompanyCreate, CompanyUpdate

class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_company(self, company: CompanyCreate, owner_user_id: str) -> Company:
        db_company = Company(
            name=company.name,
            description=company.description,
            owner_user_id=owner_user_id
        )
        self.db.add(db_company)
        self.db.commit()
        self.db.refresh(db_company)
        return db_company

    def get_company(self, company_id: int) -> Company:
        return self.db.query(Company).filter(Company.id == company_id).first()

    def get_companies(self, owner_user_id: str) -> List[Company]:
        return self.db.query(Company).filter(Company.owner_user_id == owner_user_id).all()

    def update_company(self, company_id: int, company: CompanyUpdate, owner_user_id: str) -> Company:
        db_company = self.get_company(company_id)
        if not db_company:
            return None
        if db_company.owner_user_id != owner_user_id:
            return None
        db_company.name = company.name or db_company.name
        db_company.description = company.description or db_company.description
        self.db.commit()
        self.db.refresh(db_company)
        return db_company

    def delete_company(self, company_id: int, owner_user_id: str) -> bool:
        db_company = self.get_company(company_id)
        if not db_company:
            return False
        if db_company.owner_user_id != owner_user_id:
            return False
        self.db.delete(db_company)
        self.db.commit()
        return True