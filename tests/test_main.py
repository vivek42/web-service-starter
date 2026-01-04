from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_hello_world():
    """Test the root endpoint returns Hello World"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_say_hello():
    """Test the /hello/{name} endpoint with a name parameter"""
    response = client.get("/hello/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello test"}


def test_say_hello_with_different_names():
    """Test the /hello/{name} endpoint with various names"""
    test_cases = [
        ("Alice", "Hello Alice"),
        ("Bob", "Hello Bob"),
        ("World", "Hello World"),
        ("John Doe", "Hello John Doe"),
    ]
    
    for name, expected_message in test_cases:
        response = client.get(f"/hello/{name}")
        assert response.status_code == 200
        assert response.json() == {"message": expected_message}


def test_say_hello_with_special_characters():
    """Test the /hello/{name} endpoint handles URL-encoded characters"""
    response = client.get("/hello/test%20user")
    assert response.status_code == 200
    # URL decoding happens automatically, so "test user" should be the name
    assert "test user" in response.json()["message"]

