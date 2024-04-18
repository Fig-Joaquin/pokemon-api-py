from pymongo import MongoClient
import json
from bson import ObjectId
import os

userCollection = "pokemondb"

def import_colecction():
    # Conectarse a la base de datos
    client = MongoClient("mongodb://localhost:27017/")
    db = client.test 
    # Constant
    INTRO_TIME = "Presione Enter para continuar..."

    # Obtener y desplegar las colecciones disponibles
    collections = db.list_collection_names()
    print("Colecciones disponibles en la base de datos:")
    for collection in collections:
        print(collection)

    # Solicitar al usuario que ingrese el nombre de la colección
    option = input("\n Se creara una colección con el nombre: pokemondb. El pograma trabajará con esa colección.\n  ¿Deseas continuar? si/no para continuar...\n:").lower()
    if option == "no":
        exit_program = True
    if option == "si":
        exit_program = False

    # Si el usuario decide no salir, continuar con el flujo del programa
    if not exit_program:
        # Colección elegida por el usuario
        collectionChosen = db[userCollection]

        # Solicitar al usuario que ingrese el nombre del archivo JSON
        nombre_archivo = input("Por favor, ingresa el nombre del archivo JSON que insertarás en la colección. \nEl archivo debe estar dentro de la carpeta files - Ejemplo: archivo.json\n")
        
        # Construir la ruta completa del archivo JSON en la carpeta json-files
        ruta_archivo = os.path.join("files", nombre_archivo)

        # Verificar si el archivo existe
        if os.path.exists(ruta_archivo):
            # Abrir el archivo JSON proporcionado por el usuario
            with open(ruta_archivo, 'r') as archivo:
                datos_perros = json.load(archivo)
            # Insertar los documentos en la nueva colección
            resultado = collectionChosen.insert_many(datos_perros)
            # Imprimir el número de documentos insertados
            print("Se insertaron", len(resultado.inserted_ids), "documentos en la colección '", userCollection, "'.")
        else:
            print("El archivo JSON especificado no existe en la carpeta 'files'.")
        input(INTRO_TIME)

if __name__ == "__main__":
    import_colecction()
