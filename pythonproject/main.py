import requests
import json

token = 'd7c725e6fa42ab07d9f9c672f7285917'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
     "name": "Мой покемон",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={

    "pokemon_id": 2690,
    "name": "NewName",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response_put.text)

response_post1 = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token': token}, json={
    "pokemon_id": "2690",
    "name": "NewName"
})

print(response_post1.text)


