from sqlalchemy.orm import Session
from ..repositories.product_repository import ProductRepository
from ..schemas.product_schema import LoanProductCreate, LoanProductUpdate
from fastapi import HTTPException

class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)

    def create_product(self, product_data: LoanProductCreate):
        return self.repository.create(product_data)

    def get_product(self, product_id: int):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def list_products(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)

    def update_product(self, product_id: int, product_data: LoanProductUpdate):
        return self.repository.update(product_id, product_data)

    def delete_product(self, product_id: int):
        if not self.repository.delete(product_id):
            raise HTTPException(status_code=404, detail="Product not found")
        return {"message": "Product deleted successfully"}
