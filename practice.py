import requests

api_key = 'f6dd825d-9051-4b6e-be99-221369439e80'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

response = requests.get(url)

definitions = response.json()

for definition in definitions:
    print(definition)