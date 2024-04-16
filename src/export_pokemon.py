import json
import os

# Ruta a guardar el archivo. Se guarda en la carpeta src/files
file_path = os.path.join("src", "files", "pokemonDataBase.json")

def export_to_json(pokemon_data):
    # Verificar si el archivo ya existe
    if os.path.exists(file_path):
        # Si el archivo existe, cargar los datos actuales
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        # Verificar si los datos cargados son una lista
        if not isinstance(data, list):
            # Si no es una lista, inicializarla como una lista vacía
            data = []
    else:
        # Si el archivo no existe, crear una lista vacía
        data = []

    # Agregar los datos del nuevo Pokémon a los datos existentes
    data.append(pokemon_data)

    # Escribir los datos combinados en el archivo JSON
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"La información del Pokémon {pokemon_data} se ha añadido al archivo {file_path}")