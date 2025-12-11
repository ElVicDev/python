# Logs
""" El registro es la práctica de anotar detalles sobre excepciones y 
    otros eventos en tu código. 
    Esto crea un registro histórico que es inestimable para depurar y 
    entender cómo se comporta tu aplicación en el mundo real. """

import logging

try:
    # Your potentially error-prone code here
    result = 10 / 0
except Exception as e:
    logging.error(f"An error occurred: {e}")  # Logs the exception with details

""" El registro proporciona contexto, facilitando la localización de la 
    causa raíz de los problemas. 
    Es como dejar un rastro de migas de pan que tú mismo u otros desarrolladores 
    pueden seguir cuando investigan problemas. """