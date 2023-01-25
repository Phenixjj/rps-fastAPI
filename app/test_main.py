from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_good_choice():
    response = client.post("/play", json={"myHand": "rock"})
    assert response.status_code == 418 or 201 or 204

def test_bad_choice():
    response = client.post("/play", json={"myHand": "marmotte"})
    assert response.status_code == 400

def test_get_results():
    response = client.get("/results")
    assert response.status_code == 200
    assert response.content == b'[]'

def test_reset():
    response = client.get("/reset")
    assert response.status_code == 200
