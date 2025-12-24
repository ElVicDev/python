# Generación de archivos de registro

import logging
logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
def divide(x, y):
    try:
        result = x / y
        logging.info(f"Successfully divided {x} by {y} to get {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted!")
        return None
divide(10, 2)
divide(5, 0)

""" Este código creará un Archivo de registro 'myapp.log' con entradas como:

    INFO: Successfully divided 10 by 2 to get 5.0

    ERROR: Division by zero attempted! """