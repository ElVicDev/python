# Exceptions
""" Es crucial manejar las excepciones de forma proactiva, especialmente cuando 
    se interactúa con recursos externos (archivos, bases de datos, API). 
    Si registra los errores, proporciona mensajes claros y realiza pruebas 
    exhaustivas, creará aplicaciones más estables, fiables y fáciles de usar. """

import logging

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    logging.error(f"KeyError encountered: {e}")
    # Handle the error or provide a fallback mechanism