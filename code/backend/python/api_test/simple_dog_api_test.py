import requests

url_path = "https://api.thedogapi.com/v1/images/search"

def test_returns_status_200():
    response = requests.get(url_path)
    assert response.status_code == 200, "API should return HTTP 200"
    
def test_returns_list():
    response = requests.get(url_path)
    data = response.json()

    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "List should not be empty"
    
def test_returns_required_fields():
    response = requests.get(url_path)
    data = response.json()

    required_fields = {"id", "url", "width", "height"}

    for item in data:
        assert all(field in item for field in required_fields), "Missing required fields"