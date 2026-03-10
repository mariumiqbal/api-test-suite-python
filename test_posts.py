import requests

def test_get_valid_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["userId"] is not None
    assert data["body"] is not None
    assert data["title"] is not None
    assert len(data["title"]) > 0
    assert isinstance(data["title"], str)
    assert isinstance(data["id"], int)
    assert isinstance(data["userId"], int)

def test_get_invalid_post(base_url):
    response = requests.get(f"{base_url}/posts/999")
    assert response.status_code == 404