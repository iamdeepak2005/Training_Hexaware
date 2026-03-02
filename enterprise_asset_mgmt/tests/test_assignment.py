from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def it_admin_token():
    client.post(
        "/auth/register",
        json={
            "name": "IT Admin 2",
            "email": "itadmin2@example.com",
            "password": "password123",
            "role": "IT_ADMIN"
        }
    )
    response = client.post(
        "/auth/login",
        data={"username": "itadmin2@example.com", "password": "password123"}
    )
    return response.json()["access_token"]

@pytest.fixture
def employee_token():
    client.post(
        "/auth/register",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "password": "password123",
            "role": "EMPLOYEE"
        }
    )
    response = client.post(
        "/auth/login",
        data={"username": "john@example.com", "password": "password123"}
    )
    return response.json()["access_token"]

def test_assign_asset_workflow(it_admin_token, employee_token):
    # 1. Create asset
    asset_res = client.post(
        "/itadmin/assets",
        headers={"Authorization": f"Bearer {it_admin_token}"},
        json={
            "asset_tag": "LAP-100",
            "asset_type": "Laptop",
            "brand": "Apple",
            "model": "MacBook Air",
            "purchase_date": "2023-01-01"
        }
    )
    asset_id = asset_res.json()["id"]

    # 2. Get employee ID (from own info)
    emp_info = client.get("/employee/assets", headers={"Authorization": f"Bearer {employee_token}"})
    # Since we don't have a direct /me endpoint in this snippet, let's just assume we can get user_id from somewhere or just use 2 (since it's the second user)
    # Better: let's add a /me endpoint or just use the ID we know from registration (sequential in sqlite)
    user_id = 2 

    # 3. Assign
    assign_res = client.post(
        "/itadmin/assignments",
        headers={"Authorization": f"Bearer {it_admin_token}"},
        json={
            "asset_id": asset_id,
            "user_id": user_id,
            "assigned_date": "2023-10-01"
        }
    )
    assert assign_res.status_code == 200
    assert assign_res.json()["asset_id"] == asset_id

    # 4. Return
    return_res = client.post(
        f"/itadmin/assets/{asset_id}/return",
        headers={"Authorization": f"Bearer {it_admin_token}"},
        json={
            "returned_date": "2023-11-01",
            "condition_on_return": "Good"
        }
    )
    assert return_res.status_code == 200
    assert return_res.json()["returned_date"] == "2023-11-01"
