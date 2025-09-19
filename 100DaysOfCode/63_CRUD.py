""" Day 63: CRUD application
Build a basic CRUD (Create, Read, Update, Delete) application. """

from flask import Flask, request, jsonify, abort
app = Flask(__name__)
data = {}
@app.route('/items', methods=['POST'])
def create_item():
    item = request.json
    item_id = len(data) + 1
    data[item_id] = item
    return jsonify({"id": item_id}), 201
@app.route('/items/<int:item_id>', methods=['GET'])
def read_item(item_id):
    item = data.get(item_id)
    if not item:
        abort(404)
    return jsonify(item)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.json
    if item_id not in data:
        abort(404)
    data[item_id] = item
    return jsonify(item)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in data:
        abort(404)
    del data[item_id]
    return '', 204
if __name__ == '__main__':
    app.run(debug=True)

# Output:
# Al ejecutar el script, se iniciará un servidor web local.
# Puede usar herramientas como Postman o curl para probar las operaciones CRUD:
# - Crear un ítem: POST http://localhost:5000/items con un cuerpo JSON.
# - Leer un ítem: GET http://localhost:5000/items/1
# - Actualizar un ítem: PUT http://localhost:5000/items/1 con un cuerpo JSON.
# - Eliminar un ítem: DELETE http://localhost:5000/items/1

# Comparación con el código del día 62:
# El código del día 62 crea un servidor web simple usando Flask,
# mientras que este código del día 63 implementa una aplicación CRUD básica.