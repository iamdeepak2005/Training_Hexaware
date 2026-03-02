from sqlalchemy.orm import Session
from app.repositories.asset_repo import AssetRepo
from app.schemas.asset_schema import AssetCreate, AssetUpdate
from app.core.pagination import paginate

class AssetService:
    def __init__(self, db: Session):
        self.asset_repo = AssetRepo(db)

    def create_asset(self, asset_data: AssetCreate):
        existing_asset = self.asset_repo.get_asset_by_tag(asset_data.asset_tag)
        if existing_asset:
            raise ValueError("Asset with this tag already exists")
        return self.asset_repo.create_asset(asset_data)

    def get_assets(self, page: int = 1, size: int = 20, status: str = None, department_id: int = None):
        skip = (page - 1) * size
        assets = self.asset_repo.get_all_assets(skip=skip, limit=size, status=status, department_id=department_id)
        total = self.asset_repo.get_total_count(status=status, department_id=department_id)
        return paginate(assets, total, page, size)

    def get_asset_by_id(self, asset_id: int):
        return self.asset_repo.get_asset_by_id(asset_id)
