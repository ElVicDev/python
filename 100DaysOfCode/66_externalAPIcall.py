""" Día 66: Llamada de API externa
Obtenga datos de una API externa y visualelo en una página web. """

import requests
from flask import Flask, render_template_string
app = Flask(__name__)
@app.route('/')
def home():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    price = data['bpi']['USD']['rate']
    html = f"""
    <html>
        <head><title>Bitcoin Price</title></head>
        <body>
            <h1>Current Bitcoin Price</h1>
            <p>USD: {price}</p>
        </body>
    </html>
    """
    return render_template_string(html)
if __name__ == '__main__':
    app.run(debug=True)

# Output:
# Al ejecutar el script, se iniciará un servidor web local.
# Al abrir http://localhost:5000 en un navegador,
# verá la página que muestra el precio actual de Bitcoin en USD.

# Comparación con el código del día 65:
# El código del día 65 crea una API RESTful utilizando Flask-RESTful,
# mientras que este código del día 66 obtiene datos de una API externa
# y los muestra en una página web simple.