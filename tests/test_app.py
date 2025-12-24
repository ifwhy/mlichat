import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "MliChat" in response.text


def test_create_room(client):
    response = client.get("/api/room/create")
    assert response.status_code == 200
    data = response.json()
    assert "room_id" in data
    assert len(data["room_id"]) == 8


def test_room_page(client):
    create_response = client.get("/api/room/create")
    room_id = create_response.json()["room_id"]
    
    response = client.get(f"/room/{room_id}?name=TestUser")
    assert response.status_code == 200
    assert room_id in response.text
