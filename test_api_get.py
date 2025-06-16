import requests
import pytest

@pytest.fixture
def base_url():
    return "https://petstore.swagger.io/v2/pet/100"

def test_get_method(base_url):
    headers = {'accept': 'application/json'}
    response = requests.get(base_url, headers=headers)
    print("Full response:", response.json()) # Debugging line to print the full response

    assert response.status_code == 201, f"Expected status code 200, got {response.status_code}"
    assert len(response.json()) > 0, "Response data is empty"

