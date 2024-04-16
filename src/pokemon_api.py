import requests

API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_info(pokemon_name):
    response = requests.get(f'{API_URL}{pokemon_name}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener información del Pokémon {pokemon_name}. Código de estado: {response.status_code}")
        return None

def create_pokemon_data(pokemon_info):
    if pokemon_info:
        pokemon_data = {
            "Número en la pokedex": pokemon_info["id"],
            "Habilidades": [ability['ability']['name'] for ability in pokemon_info["abilities"]],
            "Nombre": pokemon_info["name"],
            "Altura": pokemon_info["height"],
            "Peso": pokemon_info["weight"],
            "Tipos": [t["type"]["name"] for t in pokemon_info["types"]],
            "Estadisticas": {stat['stat']['name']: stat['base_stat'] for stat in pokemon_info["stats"]}
        }
        return pokemon_data
    else:
        return None
