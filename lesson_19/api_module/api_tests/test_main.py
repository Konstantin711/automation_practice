import requests



def test_get():
    response = requests.get("https://reqres.in/api/users?page=1")
    print(response.text)