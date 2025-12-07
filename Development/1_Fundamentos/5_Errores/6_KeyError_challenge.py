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

    # Ejemplo 1:
"""
city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
city_name = "New York"
Debería obtener la población de Nueva York, que es 8336817 en este diccionario.
"""
    # Ejemplo 2:
"""
city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
city_name = "Tampa"
Esto debería producir un KeyError indicando 'Ciudad "Tampa" no encontrada en los datos de población.'
"""

def get_city_population(populations, city):
    try:
        # Intenta acceder a la población de la ciudad
        population = populations[city]
        return population
    except KeyError:
        # Captura el KeyError si la clave (ciudad) no se encuentra
        error_message = f'City "{city}" not found in population data.'
        # Lanza explícitamente un nuevo KeyError con el mensaje personalizado
        raise KeyError(error_message)
    
city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

# Ejemplo 1: Ciudad encontrada (Devuelve la población):
city_name = "New York"
try:
    population = get_city_population(city_populations, city_name)
    print(f"The population of {city_name} is {population}")
except KeyError as e:
    print(f"{e}")

# Ejemplo 2: Ciudad no encontrada (Lanza KeyError)
city_name = "Tampa"
try:
    population = get_city_population(city_populations, city_name)
    print(f"The population of {city_name} is {population}")
except KeyError as e:
    # El mensaje de error que se imprime aquí es el mensaje personalizado
    print(f"{e}")