import requests

print("\n\n\n\n\n")
URL = "https://api.chess.com/pub/player/the_only_bollock"

request = requests.get(URL)
request_json = request.json()

print(request_json)