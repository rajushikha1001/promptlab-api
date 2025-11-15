from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summary():
    response = client.post("/summarize", json={"input_text": "This is a long paragraph."})
    assert response.status_code == 200
