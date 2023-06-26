from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_rides():
    response = client.get("/rides")
    assert response.status_code == 200

