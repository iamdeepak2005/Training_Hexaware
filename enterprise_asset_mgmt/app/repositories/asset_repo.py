from sqlalchemy.orm import Session
from app.models.asset import Asset, AssetStatus
from app.schemas.asset_schema import AssetCreate, AssetUpdate

class AssetRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_asset(self, asset_data: AssetCreate):
        db_asset = Asset(**asset_data.dict())
        self.db.add(db_asset)
        self.db.commit()
        self.db.refresh(db_asset)
        return db_asset

    def get_asset_by_id(self, asset_id: int):
        return self.db.query(Asset).filter(Asset.id == asset_id).first()

    def get_asset_by_tag(self, asset_tag: str):
        return self.db.query(Asset).filter(Asset.asset_tag == asset_tag).first()

    def update_asset_status(self, asset_id: int, status: AssetStatus):
        asset = self.get_asset_by_id(asset_id)
        if asset:
            asset.status = status
            self.db.commit()
            self.db.refresh(asset)
        return asset

    def get_all_assets(self, skip: int = 0, limit: int = 100, status: str = None, department_id: int = None):
        query = self.db.query(Asset)
        if status:
            query = query.filter(Asset.status == status)
        if department_id:
            query = query.filter(Asset.department_id == department_id)
        return query.offset(skip).limit(limit).all()

    def get_total_count(self, status: str = None, department_id: int = None):
        query = self.db.query(Asset)
        if status:
            query = query.filter(Asset.status == status)
        if department_id:
            query = query.filter(Asset.department_id == department_id)
        return query.count()
