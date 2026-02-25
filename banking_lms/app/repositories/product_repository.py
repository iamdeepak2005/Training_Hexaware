from sqlalchemy.orm import Session
from ..models.loan_product import LoanProduct
from ..schemas.product_schema import LoanProductCreate, LoanProductUpdate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id: int):
        return self.db.query(LoanProduct).filter(LoanProduct.id == product_id).first()

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(LoanProduct).offset(skip).limit(limit).all()

    def create(self, product: LoanProductCreate):
        db_product = LoanProduct(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def update(self, product_id: int, product_data: LoanProductUpdate):
        db_product = self.get_by_id(product_id)
        if db_product:
            for key, value in product_data.dict(exclude_unset=True).items():
                setattr(db_product, key, value)
            self.db.commit()
            self.db.refresh(db_product)
        return db_product

    def delete(self, product_id: int):
        db_product = self.get_by_id(product_id)
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
            return True
        return False
