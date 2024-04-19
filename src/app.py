from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['pokemondb']

# Ruta para la página principal que mostrará los gráficos
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener datos para el gráfico de barras
@app.route('/data/bar-chart', methods=['GET'])
def get_bar_chart_data():
    pokemon_types = {}
    for pokemon in collection.find({}, {'_id': 0, 'tipos': 1}):
        for p_type in pokemon['tipos']:
            if p_type in pokemon_types:
                pokemon_types[p_type] += 1
            else:
                pokemon_types[p_type] = 1
    return jsonify(pokemon_types)

# Ruta para obtener datos para el gráfico de dispersión
@app.route('/data/scatter-plot', methods=['GET'])
def get_scatter_plot_data():
    scatter_data = []
    for pokemon in collection.find({}, {'_id': 0, 'nombre': 1, 'altura': 1, 'peso': 1}):
        scatter_data.append({'nombre': pokemon['nombre'], 'altura': pokemon['altura'], 'peso': pokemon['peso']})
    return jsonify(scatter_data)

# Ruta para obtener todos los Pokémon
@app.route('/pokemon', methods=['GET'])
def get_all_pokemon():
    pokemon_list = list(collection.find({}, {'_id': 0}))
    return jsonify(pokemon_list)

# Ruta para obtener un Pokémon por su ID de la Pokédex
@app.route('/pokemon/<int:pokedex_id>', methods=['GET'])
def get_pokemon_by_id(pokedex_id):
    pokemon = collection.find_one({'pokedex_id': pokedex_id},{'_id': 0})
    if pokemon:
        return jsonify(pokemon)
    else:
        return jsonify({'message': 'Pokémon no encontrado'}), 404

# Ruta para obtener un Pokémon por su nombre
@app.route('/pokemon/<string:nombre>', methods=['GET'])
def get_pokemon_by_name(nombre):
    pokemon = collection.find_one({'nombre': nombre}, {'_id': 0})
    if pokemon:
        return jsonify(pokemon)
    else:
        return jsonify({'message': 'Pokémon no encontrado'}), 404

# Ruta para obtener datos para el gráfico de pastel
@app.route('/data/pie-chart', methods=['GET'])
def get_pie_chart_data():
    pokemon_types = {}
    for pokemon in collection.find({}, {'_id': 0, 'tipos': 1}):
        for p_type in pokemon['tipos']:
            if p_type in pokemon_types:
                pokemon_types[p_type] += 1
            else:
                pokemon_types[p_type] = 1
    return jsonify(pokemon_types)
# Ruta para obtener datos para el gráfico de línea (promedio de pesos de Pokémon)
@app.route('/data/average-weight', methods=['GET'])
def get_average_weight_data():
    weight_data = [pokemon['peso'] for pokemon in collection.find({}, {'_id': 0, 'peso': 1})]
    average_weight = sum(weight_data) / len(weight_data)
    return jsonify({'average_weight': average_weight})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
