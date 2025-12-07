# Reto de código funcional: Manejar una KeyError

""" Escribe una función Python llamada get_city_population que tome dos parámetros.
        populations - un diccionario que representa poblaciones de ciudades.
        city - una cadena que representa el nombre de la ciudad.

    La función debería:
    - Devolver la población de la ciudad especificada si se encuentra en el diccionario.
    - Lanzar un mensaje de error claro en KeyError si no se encuentra la ciudad.
    - Usar un bloque try-except dentro de la función para manejar el KeyError 
        con un mensaje de error personalizado.

Consejos:
    - Utilice raise KeyError() para lanzar explícitamente la excepción con su mensaje 
        de error personalizado.
    - No utilice ninguna sugerencia de tipo al declarar la función. """

def get_city_population(populations, city):
    try:
        return populations[city]
    except KeyError:
        raise KeyError(f"La ciudad '{city}' no se encuentra en el diccionario de poblaciones.")

city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
try:
    print(get_city_population(city_populations, "Tampa"))
except KeyError as e:
    print(e)
    # Manejar el error o proporcionar un mecanismo alternativo
try:
    print(get_city_population(city_populations, "New York"))
except KeyError as e:
    print(e)