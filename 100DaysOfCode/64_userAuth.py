""" Día 64: Autenticación del usuario
Implementar la autenticación del usuario en una aplicación web. """

from flask import Flask, request, jsonify, abort, session
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.secret_key

users = {}
@app.route('/register', methods=['POST'])
def register():
    user = request.json
    username = user.get('username')
    password = user.get('password')
    if username in users:
        abort(400, 'User already exists')
    users[username] = generate_password_hash(password)
    return jsonify({"message": "User registered"}), 201
@app.route('/login', methods=['POST'])
def login():
    user = request.json
    username = user.get('username')
    password = user.get('password')
    stored_password = users.get(username)
    if not stored_password or not check_password_hash(stored_password, password):
        abort(401, 'Invalid credentials')
    session['user'] = username
    return jsonify({"message": "Logged in"}), 200
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "Logged out"}), 200
@app.route('/protected', methods=['GET'])
def protected():
    if 'user' not in session:
        abort(401, 'Unauthorized')
    return jsonify({"message": f"Hello, {session['user']}!"}), 200
if __name__ == '__main__':
    app.run(debug=True)

# Output:
# Al ejecutar el script, se iniciará un servidor web local.
# Puede usar herramientas como Postman o curl para probar las 
# operaciones de autenticación:
# - Registrar un usuario: 
# POST http://localhost:5000/register con un cuerpo JSON 
# {"  username": "user1", "password": "pass123"}.
# - Iniciar sesión: 
# POST http://localhost:5000/login con un cuerpo JSON 
# {"  username": "user1", "password": "pass123"}.
# - Acceder a una ruta protegida: GET http://localhost:5000/protected
# - Cerrar sesión: POST http://localhost:5000/logout
# Comparación con el código del día 63:
# El código del día 63 implementa una aplicación CRUD básica,
# mientras que este código del día 64 añade autenticación de 
# usuario a una aplicación web.