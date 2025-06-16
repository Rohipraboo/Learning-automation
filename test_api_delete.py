import requests
import pytest
import json
import os

@pytest.fixture
def base_url():
    config_path = "config.json"
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"{config_path} not found. Please create it with a 'base_url' key.")
    with open(config_path) as f:
        config = json.load(f)
    if "base_url" not in config:
        raise KeyError("'base_url' key not found in config.json.")
    return config["base_url"]

def test_delete_method(base_url):
    headers = {'accept': 'application/json'}
    url = f"{base_url}/400"
    response = requests.delete(url, headers=headers)
    print("Request URL:", url)
    print("Response status code:", response.status_code)
    print("Response content:", response.text)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
