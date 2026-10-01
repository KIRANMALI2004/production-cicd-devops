import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Production CI/CD DevOps" in response.data
    assert b"Application is Running" in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_info():
    client = app.test_client()

    response = client.get("/api/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "Production CI/CD Pipeline"