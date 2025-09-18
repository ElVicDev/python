""" Día 62: servidor web
Cree un servidor web simple usando Flask o Django. """

from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "¡Hola, Mundo! Este es un servidor web simple usando Flask."
if __name__ == '__main__':
    app.run(debug=True)

# Output:
# Al ejecutar el script, se iniciará un servidor web local.
# Puede acceder a él en http://localhost:5000 y verá el mensaje 
# "¡Hola, Mundo! Este es un servidor web simple usando Flask."
# Comparación con el código del día 61:
# El código del día 61 implementa programación dinámica para calcular 
# números de Fibonacci, mientras que este código del día 62 crea 
# un servidor web simple usando Flask.