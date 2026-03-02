from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "name": "Super Admin",
            "email": "admin@example.com",
            "password": "password123",
            "role": "SUPERADMIN"
        }
    )
    assert response.status_code == 200
    assert response.json()["email"] == "admin@example.com"

def test_login_user():
    response = client.post(
        "/auth/login",
        data={"username": "admin@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
