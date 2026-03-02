from sqlalchemy.orm import Session
from app.models.asset_assignment import AssetAssignment
from app.schemas.assignment_schema import AssignmentCreate, AssignmentReturn
from datetime import date

class AssignmentRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_assignment(self, assign_data: AssignmentCreate):
        db_assign = AssetAssignment(**assign_data.dict())
        self.db.add(db_assign)
        self.db.commit()
        self.db.refresh(db_assign)
        return db_assign

    def get_active_assignment_by_asset(self, asset_id: int):
        return self.db.query(AssetAssignment).filter(
            AssetAssignment.asset_id == asset_id,
            AssetAssignment.returned_date == None
        ).first()

    def update_assignment_return(self, assignment_id: int, return_data: AssignmentReturn):
        db_assign = self.db.query(AssetAssignment).filter(AssetAssignment.id == assignment_id).first()
        if db_assign:
            db_assign.returned_date = return_data.returned_date
            db_assign.condition_on_return = return_data.condition_on_return
            self.db.commit()
            self.db.refresh(db_assign)
        return db_assign

    def get_all_assignments(self, user_id: int = None, asset_id: int = None):
        query = self.db.query(AssetAssignment)
        if user_id:
            query = query.filter(AssetAssignment.user_id == user_id)
        if asset_id:
            query = query.filter(AssetAssignment.asset_id == asset_id)
        return query.all()
