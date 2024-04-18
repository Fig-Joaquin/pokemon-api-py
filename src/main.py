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
        if option_buscar == "no":
            break

def main():
    while True:
        # Solicitar al usuario el nombre de un Pokémon
        option = input("\nExtraer pokémon de la api y exportarlos en un json. : Extraer\nPara buscar pokemon: buscar\n Exportar pokemon: exportar\nPara salir del programa: salir\n: ").lower()
        
        if option == "salir":
            break
        if option == "buscar":
            search_option()
        if option == "extraer":
            _, status_code = catch_pokemon_api.get_all_pokemon()
            if status_code == 200:
                print("La exportación de los Pokémon fue exitosa.")
            else:
                print("Error al exportar los Pokémon. Código de estado:", status_code)
        if option == "importar":
            import_colecction.import_colecction()
        if option == "mostrar":
            read_pokemon.read_data()
        if option == "graficos":
            app.app.run(debug=True)

if __name__ == "__main__":
    main()
