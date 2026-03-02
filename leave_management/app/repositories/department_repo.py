from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate

class DepartmentRepository:
    def get_by_id(self, db: Session, dept_id: int):
        return db.query(Department).filter(Department.id == dept_id).first()

    def get_all(self, db: Session):
        return db.query(Department).all()

    def create(self, db: Session, dept: DepartmentCreate):
        db_dept = Department(name=dept.name, manager_id=dept.manager_id)
        db.add(db_dept)
        db.commit()
        db.refresh(db_dept)
        return db_dept

    def update_manager(self, db: Session, db_dept: Department, manager_id: int):
        db_dept.manager_id = manager_id
        db.commit()
        db.refresh(db_dept)
        return db_dept

department_repo = DepartmentRepository()
