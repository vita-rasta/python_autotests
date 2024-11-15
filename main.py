import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '513f90cb2fa7c89ff89ffb21b5419dbb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create_pokemons = {
    "name": "generate",
    "photo_id": -1
}

create_pokemons = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create_pokemons)
print(create_pokemons.text)

body_rename_pokemons = {
    "pokemon_id": create_pokemons.json()['id'],
    "name": "generate"
}

body_catch_pokeball = {
    "pokemon_id": create_pokemons.json()['id']
}

rename_pokemons = requests.patch(url = f'{URL}pokemons', headers = HEADER, json = body_rename_pokemons)
print(rename_pokemons.text)

rename_pokemons = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_catch_pokeball)
print(rename_pokemons.text)