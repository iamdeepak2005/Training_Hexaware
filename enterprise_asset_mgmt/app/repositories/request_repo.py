from sqlalchemy.orm import Session
from app.models.asset_request import AssetRequest, RequestStatus
from app.schemas.request_schema import RequestCreate, RequestUpdate

class RequestRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_request(self, req_data: RequestCreate, employee_id: int):
        db_req = AssetRequest(**req_data.dict(), employee_id=employee_id)
        self.db.add(db_req)
        self.db.commit()
        self.db.refresh(db_req)
        return db_req

    def get_request_by_id(self, req_id: int):
        return self.db.query(AssetRequest).filter(AssetRequest.id == req_id).first()

    def update_request_status(self, req_id: int, update_data: RequestUpdate):
        db_req = self.get_request_by_id(req_id)
        if db_req:
            db_req.status = update_data.status
            db_req.approved_by = update_data.approved_by
            self.db.commit()
            self.db.refresh(db_req)
        return db_req

    def get_all_requests(self, employee_id: int = None, status: str = None):
        query = self.db.query(AssetRequest)
        if employee_id:
            query = query.filter(AssetRequest.employee_id == employee_id)
        if status:
            query = query.filter(AssetRequest.status == status)
        return query.all()
