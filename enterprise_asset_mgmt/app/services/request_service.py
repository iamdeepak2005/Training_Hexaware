from sqlalchemy.orm import Session
from app.repositories.request_repo import RequestRepo
from app.schemas.request_schema import RequestCreate, RequestUpdate, RequestStatus
from app.services.assignment_service import AssignmentService
from app.schemas.assignment_schema import AssignmentCreate
from datetime import date

class RequestService:
    def __init__(self, db: Session):
        self.request_repo = RequestRepo(db)
        self.assignment_service = AssignmentService(db)

    def create_request(self, req_data: RequestCreate, employee_id: int):
        return self.request_repo.create_request(req_data, employee_id)

    def approve_request(self, req_id: int, admin_id: int):
        update_data = RequestUpdate(status=RequestStatus.APPROVED, approved_by=admin_id)
        return self.request_repo.update_request_status(req_id, update_data)

    def reject_request(self, req_id: int, admin_id: int):
        update_data = RequestUpdate(status=RequestStatus.REJECTED, approved_by=admin_id)
        return self.request_repo.update_request_status(req_id, update_data)

    def get_all_requests(self, employee_id=None, status=None):
        return self.request_repo.get_all_requests(employee_id=employee_id, status=status)
