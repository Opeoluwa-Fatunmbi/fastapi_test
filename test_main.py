from fastapi.testclient import TestClient
from main import app
from fastapi import status


client = TestClient(app=app)


def test_index():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}

def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "product",
            "description": "description",
            "price": 9.99,
            "tax": 0.99
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "name": "product",
        "description": "description",
        "price": 9.99,
        "tax": 0.99
    }