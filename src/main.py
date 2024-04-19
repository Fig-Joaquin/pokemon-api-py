import pokemon_api
import export_pokemon
import catch_pokemon_api
import import_colecction
import read_pokemon
import app
def search_option():
    while True:
        pokemon_name = input("Introduce el nombre de un Pokémon: ").lower()
    # Obtener información del Pokémon desde la API
        pokemon_info = pokemon_api.get_pokemon_info(pokemon_name)
        option_buscar = input("Desea exportar este pokemon? si/no: ").lower()
        if option_buscar == "si":
    # Crear datos del Pokémon
            pokemon_data = pokemon_api.create_pokemon_data(pokemon_info)
    # Exportar datos del Pokémon a un archivo JSON
            export_pokemon.export_to_json(pokemon_data)
            break
        if option_buscar == "no":
            break

def extract_pokemon():
    _, status_code = catch_pokemon_api.get_all_pokemon()
    if status_code == 200:
        print("La exportación de los Pokémon fue exitosa.")
    else:
        print("Error al exportar los Pokémon. Código de estado:", status_code)
def main():
    print("Menú!")
    print("\nEscribir la opción que se desea realizar")
    while True:
        # Solicitar al usuario el nombre de un Pokémon
        option = input("\nExtraer datos de la api y exportarlos en un json: extraer\nPara buscar un Pokémon específico: buscar\nImportar la colección extraída: importar\nIniciar el servidor: iniciar\nPara salir del programa: salir \n: ").lower()
        
        if option == "salir":
            break
        elif option == "buscar":
            search_option()
        elif option == "extraer":
            extract_pokemon()
        elif option == "importar":
            import_colecction.import_colecction()
        elif option == "mostrar":
            read_pokemon.read_data()
        elif option == "iniciar":
            import subprocess
            subprocess.Popen(["python3", "app.py"])
            print("El servidor Flask se ha iniciado. Puedes acceder a través del navegador web.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    main()
