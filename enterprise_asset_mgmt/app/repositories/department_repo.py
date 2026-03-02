from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate

class DepartmentRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_department(self, dep_data: DepartmentCreate):
        db_dep = Department(name=dep_data.name, manager_id=dep_data.manager_id)
        self.db.add(db_dep)
        self.db.commit()
        self.db.refresh(db_dep)
        return db_dep

    def get_department_by_id(self, dep_id: int):
        return self.db.query(Department).filter(Department.id == dep_id).first()

    def get_all_departments(self):
        return self.db.query(Department).all()
