import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app) 


def test_login_for_access_token():
    response = client.post("/token")
    assert response.status_code == 200
    data = response.json()

    assert "access_token" in data
    assert isinstance(data["access_token"], str)
