from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_technical_request():
    response = client.post(
        "/analyze",
        json={
            "message": "I cannot login to my account",
            "user_id": "u-123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "technical"
    assert data["priority"] == "medium"
    assert data["needs_human"] is True
    assert data["confidence"] >= 0.7


def test_analyze_critical_request():
    response = client.post(
        "/analyze",
        json={
            "message": "Our production API is down with 500 errors",
            "user_id": "u-456",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "technical"
    assert data["priority"] == "high"
    assert data["needs_human"] is True


def test_analyze_rejects_empty_message():
    response = client.post(
        "/analyze",
        json={
            "message": "",
        },
    )

    assert response.status_code == 422
