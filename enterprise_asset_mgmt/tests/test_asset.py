from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def auth_token():
    # Helper to get admin token
    client.post(
        "/auth/register",
        json={
            "name": "IT Admin",
            "email": "itadmin@example.com",
            "password": "password123",
            "role": "IT_ADMIN"
        }
    )
    response = client.post(
        "/auth/login",
        data={"username": "itadmin@example.com", "password": "password123"}
    )
    return response.json()["access_token"]

def test_create_asset(auth_token):
    response = client.post(
        "/itadmin/assets",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "asset_tag": "LAP-001",
            "asset_type": "Laptop",
            "brand": "Dell",
            "model": "XPS 15",
            "purchase_date": "2023-01-01",
            "status": "AVAILABLE"
        }
    )
    assert response.status_code == 200
    assert response.json()["asset_tag"] == "LAP-001"

def test_duplicate_asset_tag(auth_token):
    client.post(
        "/itadmin/assets",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "asset_tag": "LAP-002",
            "asset_type": "Laptop",
            "brand": "Dell",
            "model": "XPS 15",
            "purchase_date": "2023-01-01",
            "status": "AVAILABLE"
        }
    )
    response = client.post(
        "/itadmin/assets",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "asset_tag": "LAP-002",
            "asset_type": "Laptop",
            "brand": "Dell",
            "model": "XPS 15",
            "purchase_date": "2023-01-01",
            "status": "AVAILABLE"
        }
    )
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]
