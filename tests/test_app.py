"""Test the FastAPI app."""
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_divide_basic():
    r = client.get("/divide", params={"a": 10, "b": 2})
    assert r.json()["result"] == 5


def test_multiply():
    r = client.get("/multiply", params={"a": 3, "b": 4})
    assert r.json()["result"] == 12
