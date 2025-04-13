import requests
import json


pyyntö = ("https://api.chucknorris.io/jokes/random")
vastaus = requests.get(pyyntö).json()
try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()["value"]
        print(json.dumps(json_vastaus, indent=2))
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
