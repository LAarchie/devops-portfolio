import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_hello_returns_hello_message(client):
    res = client.get("/api/hello")
    assert res.get_json() == {"message": "Hello, World!"}


def test_health_returns_status_healthy(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "healthy"}


def test_log_button_success_with_valid_message(client):
    message = "Log test message"
    res = client.post("/api/log-button", json={"message": message})
    assert res.status_code == 200
    assert res.get_json() == {"status": "success", "message": message}


def test_log_button_fails_with_missing_message(client):
    res = client.post("/api/log-button", json={})
    assert res.status_code == 400
    assert res.get_json() == {
        "status": "error",
        "message": "No message provided",
    }
