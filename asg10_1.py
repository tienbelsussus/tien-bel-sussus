import requests


def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url).json()

    print(response["value"])  # chỉ in nội dung joke


get_joke()