import requests
from pprint import pprint


def client():
    """  test for client """
    # {'key': '32c461ad9837eba03b448585f6ab0c28310b5d88'}
    token = 'Token 0e11fba34d012117990ea5d6494087de25365ed9'

    headers = {
        'Authorization': token,
    }

    response = requests.get(
        "http://127.0.0.1:8000/api/user-profiles/", timeout=5,
        headers=headers
        )

    print("Status Code: ", response.status_code)
    response_data = response.json()
    pprint(response_data)


if __name__ == "__main__":
    client()
