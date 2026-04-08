import requests

def get_chuck_norris_joke():
    try:
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        joke = data.get('value')
        print(joke)
    except:
        print("Error")

get_chuck_norris_joke()