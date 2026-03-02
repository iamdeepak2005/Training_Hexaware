from sqlalchemy.orm import Session
from app.repositories.assignment_repo import AssignmentRepo
from app.repositories.asset_repo import AssetRepo
from app.schemas.assignment_schema import AssignmentCreate, AssignmentReturn
from app.models.asset import AssetStatus
from datetime import date

class AssignmentService:
    def __init__(self, db: Session):
        self.assignment_repo = AssignmentRepo(db)
        self.asset_repo = AssetRepo(db)

    def assign_asset(self, assign_data: AssignmentCreate):
        asset = self.asset_repo.get_asset_by_id(assign_data.asset_id)
        if not asset:
            raise ValueError("Asset not found")
        if asset.status != AssetStatus.AVAILABLE:
            raise ValueError(f"Asset is not available. Current status: {asset.status}")
        
        # Check if asset is already assigned
        active_assign = self.assignment_repo.get_active_assignment_by_asset(assign_data.asset_id)
        if active_assign:
            raise ValueError("Asset is already actively assigned")

        assignment = self.assignment_repo.create_assignment(assign_data)
        self.asset_repo.update_asset_status(assign_data.asset_id, AssetStatus.ASSIGNED)
        return assignment

    def return_asset(self, asset_id: int, return_data: AssignmentReturn):
        active_assign = self.assignment_repo.get_active_assignment_by_asset(asset_id)
        if not active_assign:
            raise ValueError("No active assignment found for this asset")

        updated_assign = self.assignment_repo.update_assignment_return(active_assign.id, return_data)
        self.asset_repo.update_asset_status(asset_id, AssetStatus.AVAILABLE)
        return updated_assign

    def get_user_assignments(self, user_id: int):
        return self.assignment_repo.get_all_assignments(user_id=user_id)
