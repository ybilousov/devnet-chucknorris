import subprocess
import requests

subprocess.call(f"pip freeze > requirements.txt", shell=True)

chuck_api = requests.get('https://api.chucknorris.io/jokes/random')
print(chuck_api.json()['value'])
