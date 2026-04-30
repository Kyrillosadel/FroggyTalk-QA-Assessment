import requests

BASE_URL = "https://example.com/api"

def test_mobile_topup_products():
    payload = {
        "phone": "+23408012345678",
        "country": "NG"
    }

    response = requests.post(f"{BASE_URL}/mobile-topup/options", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "airtime" in data
    assert "data_bundles" in data
    assert isinstance(data["airtime"], list)

