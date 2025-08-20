import requests


def get_user_details():
    url = "https://gorest.co.in/public/v2/users/8075634"

    payload = {}
    headers = {
        'Authorization': 'Bearer b9b3492b489c402fe0cd7e9299e6fc7b172ccf67407937d21904aaffba74802e'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = response.json()
    print(json_data)
    status_code = response.status_code
    assert json_data['name'] == "Anilabh Bhattathiri Esq."
    assert status_code == 200

    print(response.text)


get_user_details()