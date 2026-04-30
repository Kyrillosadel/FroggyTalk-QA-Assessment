import requests

BASE_URL = "https://example.com/api"

def test_radio_list_api():
    response = requests.get(f"{BASE_URL}/radios")
    assert response.status_code == 200
    data = response.json()
    assert "radios" in data
    assert isinstance(data["radios"], list)
