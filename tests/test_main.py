from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_send_sms():
    response = client.post("/send-sms/", json={
        "to": "+1234567890",
        "message": "Hello World"
    })
    assert response.status_code == 200
    assert "sid" in response.json()