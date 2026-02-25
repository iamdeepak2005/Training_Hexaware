from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..schemas.product_schema import LoanProductCreate, LoanProductUpdate, LoanProductOut
from ..services.product_service import ProductService
from typing import List

router = APIRouter(prefix="/loan-products", tags=["Loan Products"])

@router.post("/", response_model=LoanProductOut)
def create_product(product: LoanProductCreate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.create_product(product)

@router.get("/{id}", response_model=LoanProductOut)
def get_product(id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_product(id)

@router.get("/", response_model=List[LoanProductOut])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.list_products(skip, limit)

@router.put("/{id}", response_model=LoanProductOut)
def update_product(id: int, product: LoanProductUpdate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.update_product(id, product)

@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.delete_product(id)
