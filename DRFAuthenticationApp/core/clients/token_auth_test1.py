import requests
from pprint import pprint


def client():
    """  test for client """
    # {'key': '32c461ad9837eba03b448585f6ab0c28310b5d88'}
    credentials = {
        "username": "testusr",
        "password": "test1234..."
    }

    response = requests.post(
        "http://127.0.0.1:8000/api/dj-rest-auth/login/",
        data=credentials, timeout=5
        )

    print("Status Code: ", response.status_code)
    response_data = response.json()
    pprint(response_data)


if __name__ == "__main__":
    client()
