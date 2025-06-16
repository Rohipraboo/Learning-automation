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

def test_post_method(base_url):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    payload = {
        "id": 400,
        "category": {
            "id": 0,
            "name": "Rabbit"
        },
        "name": "rabbit",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "rabbit"
            }
        ],
        "status": "available"
    }
    response = requests.post(base_url, headers=headers, json=payload)
    if response.status_code != 200:
        print("Response content:", response.text)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    # assert response.json().get("") == "", "Invalid input"
