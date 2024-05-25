from fastapi.testclient import TestClient
from fastapi_helloworld.main import app


def test_root_path():
    client = TestClient(app=app)

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_piaic_root():
    client = TestClient(app=app)
    responce = client.get("/piaic/")

    assert responce.status_code == 200
    assert responce.json() == {"Organization": "PIAIC"}