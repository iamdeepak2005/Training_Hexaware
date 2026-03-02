from sqlalchemy.orm import Session
from app.repositories.department_repo import department_repo
from app.schemas.department_schema import DepartmentCreate
from fastapi import HTTPException

class DepartmentService:
    def create_department(self, db: Session, dept: DepartmentCreate):
        return department_repo.create(db, dept)

    def get_all_departments(self, db: Session):
        return department_repo.get_all(db)

    def assign_manager(self, db: Session, dept_id: int, manager_id: int):
        dept = department_repo.get_by_id(db, dept_id)
        if not dept:
            raise HTTPException(status_code=404, detail="Department not found")
        return department_repo.update_manager(db, dept, manager_id)

department_service = DepartmentService()
