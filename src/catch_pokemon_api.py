import requests
import json
import os

API_URL = 'https://pokeapi.co/api/v2/pokemon?limit=50'
file_path = os.path.join("files", "pokemondb.json")

def get_pokemon_info(pokemon_url):
    response = requests.get(pokemon_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener información del Pokémon. Código de estado: {response.status_code}")
        return None

def get_all_pokemon():
    response = requests.get(API_URL)
    if response.status_code == 200:
        all_pokemon = []
        for pokemon in response.json()["results"]:
            pokemon_info = get_pokemon_info(pokemon["url"])
            if pokemon_info:
                pokemon_data = {
                    "pokedex_id": pokemon_info["id"],
                    "habilidades": [ability['ability']['name'] for ability in pokemon_info["abilities"]],
                    "nombre": pokemon_info["name"],
                    "altura": pokemon_info["height"],
                    "peso": pokemon_info["weight"],
                    "tipos": [t["type"]["name"] for t in pokemon_info["types"]],
                    "estadisticas": {stat['stat']['name']: stat['base_stat'] for stat in pokemon_info["stats"]}
                }
                all_pokemon.append(pokemon_data)
        
        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                try:
                    data = json.load(json_file)
                    if not isinstance(data, list):
                        data = []
                except json.decoder.JSONDecodeError:
                    data = []
        else:
            data = []
        
        data.extend(all_pokemon)
        
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        return all_pokemon, response.status_code  # Return both all_pokemon and response status code
    else:
        print(f"Error al obtener la lista de Pokémon. Código de estado: {response.status_code}")
        return None, response.status_code  # Return None and response status code
