import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '513f90cb2fa7c89ff89ffb21b5419dbb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '10968'

def test_status_code():
    responce = requests.get(url = f'{URL}trainers')
    assert responce.status_code == 200

def test_status_code():
    my_trainer_id = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert my_trainer_id.json()['data'][0]['id'] == TRAINER_ID

