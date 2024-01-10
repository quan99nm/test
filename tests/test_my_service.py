# Create unitest for service.py ussing pytest
# start with import 
"""
using mock to test the service.py]
"""
import pytest
from unittest.mock import patch
from source.service import get_user
import requests


def test_get_user_success():
    # Test successful retrieval of user
    expected_user = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_user

        user = get_user(1)

        assert user == expected_user
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")

def test_get_user_failure():
    # Test failure to retrieve user
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        user = get_user(1)

        assert user == requests.HTTPError
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")
