import requests
from api_client import get_post
import pytest

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

def test_negative_id(base_url):
    response = requests.get(f"{base_url}/posts/-1")
    assert response.status_code == 404

def test_negative_id_raises_error(base_url):
    with pytest.raises(ValueError, match="Post ID must be a positive integer"):
        get_post(-1, base_url)    