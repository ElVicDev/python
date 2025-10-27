""" Tuplas y conjuntos en acción """

# Tuples
coordinates = (37.7749, -122.4194)  # Latitude, longitude of San Francisco
birth_date = (1990, 12, 25)       # Year, month, day

# Sets
unique_colors = {"red", "green", "blue"}
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)    # Removes duplicates

""" Las tuplas se utilizan a menudo cuando necesitas asegurarte de que los 
    datos permanecen constantes a lo largo de tu programa. 
    Por ejemplo, puedes utilizar una tupla para almacenar coordenadas 
    (latitud y longitud), ya que no querrás que cambien accidentalmente. 
    Los conjuntos son excelentes para tareas como eliminar duplicados de una 
    lista o comprobar si un elemento existe dentro de una colección. """