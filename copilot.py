# function to search for pokemon

#import requests


def search_pokemon(pokemon_name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon_name
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_pokemon_abilities(pokemon_name):
    pokemon = search_pokemon(pokemon_name)
    if pokemon is not None:
        return pokemon['abilities']
    else:
        return None


def get_pokemon_stats(pokemon_name):
    pokemon = search_pokemon(pokemon_name)
    if pokemon is not None:
        return pokemon['stats']
    else:
        return None


def get_pokemon_type(pokemon_name):
    pokemon = search_pokemon(pokemon_name)
    if pokemon is not None:
        return pokemon['types']
    else:
        return None


def get_pokemon_weight(pokemon_name):
    pokemon = search_pokemon(pokemon_name)
    if pokemon is not None:
        return pokemon['weight']
    else:
        return None


def compare_pokemon(pokemon_name1, pokemon_name2):
    pokemon1 = search_pokemon(pokemon_name1)
    pokemon2 = search_pokemon(pokemon_name2)
    if pokemon1 is not None and pokemon2 is not None:
        return pokemon1['weight'] == pokemon2['weight']
    else:
        return False


print(get_pokemon_type('pikachu'))
