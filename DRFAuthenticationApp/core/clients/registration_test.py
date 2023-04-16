import requests
from pprint import pprint


def client():
    """  test for client """
    credentials = {
        "username": "test_rest_user_2",
        "email": "test_rest_user_2@test.com",
        "password1": "test1234...",
        "password2": "test1234..."
    }

    response = requests.post(
        "http://127.0.0.1:8000/api/dj-rest-auth/registration/",
        data=credentials, timeout=5
        )

    print("Status Code: ", response.status_code)
    response_data = response.json()
    pprint(response_data)


if __name__ == "__main__":
    client()
