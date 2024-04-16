from pymongo import MongoClient
import json
import os

# Conectarse a la base de datos
client = MongoClient("mongodb://localhost:27017/")
db = client.test 
collection = db.pokemon
# Constant
INTRO_TIME = "Presione Enter para continuar..."

# Obtener y desplegar las colecciones disponibles
collections = db.list_collection_names()
print("Colecciones disponibles en la base de datos:")
for collection in collections:
    print(collection)

# Solicitar al usuario que ingrese el nombre de la colección
userCollection = input("\nPor favor, ingresa un nombre para la colección. ¡El archivo debe estar en la carpeta correspondiente.! \n Si ingresa un nombre que no existe en la base de datos, se creará una nueva colección: \n")
if userCollection == "salir":
    exit_program = True
else:
    exit_program = False

# Si el usuario decide no salir, continuar con el flujo del programa
if not exit_program:
    # Colección elegida por el usuario
    collectionChosen = db[userCollection]

    # Solicitar al usuario que ingrese el nombre del archivo JSON
    nombre_archivo = input("Por favor, ingresa el nombre del archivo JSON que insertarás en la colección. Ejemplo: archivo.json\n")
    
    # Construir la ruta completa del archivo JSON en la carpeta json-files
    ruta_archivo = os.path.join("src","files", nombre_archivo)

    # Verificar si el archivo existe
    if os.path.exists(ruta_archivo):
        # Abrir el archivo JSON proporcionado por el usuario
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            # Eliminar el campo "_id" de los documentos
        for documento in data:
            del documento['_id']
        # Insertar los documentos en la nueva colección
        resultado = collectionChosen.insert_many(data)
        # Imprimir el número de documentos insertados
        print("Se insertaron", len(resultado.inserted_ids), "documentos en la colección '", userCollection, "'.")
    else:
        print("El archivo JSON especificado no existe en la carpeta 'json-files'.")
    input(INTRO_TIME)