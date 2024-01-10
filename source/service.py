"create a get_user function using request get"
import requests

def get_user(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    if response.status_code != 200:
        return requests.HTTPError
    else:
        return response.json()