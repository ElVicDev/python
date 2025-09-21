""" Día 65: Marco de API RESTful
Cree una API RESTful con el marco de descanso Flask o Django. """

from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
data = {}
class Item(Resource):
    def get(self, item_id):
        item = data.get(item_id)
        if not item:
            abort(404)
        return jsonify(item)
    def post(self, item_id):
        if item_id in data:
            abort(400, 'Item already exists')
        item = request.json
        data[item_id] = item
        return jsonify(item), 201
    def put(self, item_id):
        if item_id not in data:
            abort(404)
        item = request.json
        data[item_id] = item
        return jsonify(item)
    def delete(self, item_id):
        if item_id not in data:
            abort(404)
        del data[item_id]
        return '', 204
api.add_resource(Item, '/items/<int:item_id>')
if __name__ == '__main__':
    app.run(debug=True)

# Output:
# Al ejecutar el script, se iniciará un servidor web local.
# Puede usar herramientas como Postman o curl para probar las operaciones CRUD:
# - Crear un ítem: POST http://localhost:5000/items/1 con un cuerpo JSON.
# - Leer un ítem: GET http://localhost:5000/items/1
# - Actualizar un ítem: PUT http://localhost:5000/items/1 con un cuerpo JSON.
# - Eliminar un ítem: DELETE http://localhost:5000/items/1

# Comparación con el código del día 64:
# El código del día 64 implementa la autenticación de usuarios,
# mientras que este código del día 65 crea una API RESTful
# utilizando Flask-RESTful.