import pymongo
import json
from bson import ObjectId


# Conectar a la base de datos local de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db["pokemondb"]

def read_data():
    # Obtener todos los documentos de la colección
    data = list(collection.find())
    # Suponiendo que "data" es una lista de documentos que incluyen campos ObjectId
    #Convertir los ObjectId a cadenas de texto
    for doc in data:
        if '_id' in doc:
            doc['_id'] = str(doc['_id'])
    # Imprimir los datos en formato JSON con indentación para una mejor legibilidad
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    read_data()