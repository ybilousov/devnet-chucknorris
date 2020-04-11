import requests

chuck_api = requests.get('https://api.chucknorris.io/jokes/random')
print(chuck_api.json()['value'])