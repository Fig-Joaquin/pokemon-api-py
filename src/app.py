from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db["pokemon"]

@app.route('/pokemon', methods=['GET'])
def get_all_pokemon():
    pokemon_list = list(collection.find())
    return jsonify(pokemon_list)

@app.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    pokemon = collection.find_one({"Número en la pokedex": pokemon_id})
    if pokemon:
        return jsonify(pokemon)
    else:
        return jsonify({"error": "Pokémon no encontrado"}), 404

@app.route('/pokemon', methods=['POST'])
def add_pokemon():
    new_pokemon = request.json
    collection.insert_one(new_pokemon)
    return jsonify({"message": "Pokémon agregado correctamente"}), 201

@app.route('/pokemon/<int:pokemon_id>', methods=['PUT'])
def update_pokemon(pokemon_id):
    updated_pokemon = request.json
    collection.replace_one({"Número en la pokedex": pokemon_id}, updated_pokemon)
    return jsonify({"message": "Pokémon actualizado correctamente"})

@app.route('/pokemon/<int:pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    collection.delete_one({"Número en la pokedex": pokemon_id})
    return jsonify({"message": "Pokémon eliminado correctamente"})

if __name__ == '__main__':
    app.run(debug=True)
