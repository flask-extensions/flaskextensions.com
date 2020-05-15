from fastapi.testclient import TestClient
from fexapi import __version__
from fexapi.api import app

client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_read_main():
    response = client.get("/docs")
    assert response.status_code == 200
