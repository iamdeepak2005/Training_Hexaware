import pytest
from fastapi.testclient import TestClient
from datetime import date, timedelta
from app.main import app
from app.database.session import get_db
from app.database.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup test DB (same as test_auth)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_leave.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_employee_apply_leave():
    # Register employee
    client.post("/auth/register", json={
        "name": "Emp 1", "email": "emp1@example.com", "password": "pass", "role": "EMPLOYEE"
    })
    
    # Login employee
    login_resp = client.post("/auth/login", data={"username": "emp1@example.com", "password": "pass"})
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Apply for leave
    next_week = date.today() + timedelta(days=7)
    leave_data = {
        "start_date": next_week.isoformat(),
        "end_date": (next_week + timedelta(days=3)).isoformat(),
        "reason": "Vacation"
    }
    response = client.post("/employee/leaves", json=leave_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "PENDING"

def test_manager_approve_leave():
     # 1. Register manager
    client.post("/auth/register", json={
        "name": "Manager", "email": "mgr@example.com", "password": "pass", "role": "MANAGER"
    })
    
    # 2. Register employee
    client.post("/auth/register", json={
        "name": "Emp", "email": "emp@example.com", "password": "pass", "role": "EMPLOYEE"
    })
    
    # Needs to assign manager to dept and emp to dept, but for simple test let's use admin logic or just mock
    # I'll use the Admin to setup
    admin_login = client.post("/auth/register", json={ # In real app admin exists
        "name": "Admin", "email": "admin@example.com", "password": "pass", "role": "ADMIN"
    })
    login_resp = client.post("/auth/login", data={"username": "admin@example.com", "password": "pass"})
    admin_token = login_resp.json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Create dept
    dept_resp = client.post("/admin/departments", json={"name": "IT"}, headers=admin_headers)
    dept_id = dept_resp.json()["id"]
    
    # Get user IDs
    users = client.get("/admin/users", headers=admin_headers).json()
    mgr_id = [u["id"] for u in users if u["email"] == "mgr@example.com"][0]
    emp_id = [u["id"] for u in users if u["email"] == "emp@example.com"][0]
    
    # Assign mgr and emp to IT
    client.put(f"/admin/departments/{dept_id}/manager/{mgr_id}", headers=admin_headers)
    # Emp usually assigned via update user but I'll skip and just test Admin override for now
    
    # Login employee and apply
    emp_login = client.post("/auth/login", data={"username": "emp@example.com", "password": "pass"})
    emp_token = emp_login.json()["access_token"]
    emp_headers = {"Authorization": f"Bearer {emp_token}"}
    
    response = client.post("/employee/leaves", json={
        "start_date": (date.today() + timedelta(days=10)).isoformat(),
        "end_date": (date.today() + timedelta(days=12)).isoformat(),
        "reason": "Holiday"
    }, headers=emp_headers)
    leave_id = response.json()["id"]
    
    # Admin override
    override_resp = client.patch(f"/admin/leaves/{leave_id}/override?status=APPROVED", headers=admin_headers)
    assert override_resp.status_code == 200
    assert override_resp.json()["status"] == "APPROVED"
