""" Día 37: Manejar las excepciones II
Manejar excepciones para el archivo no encontrado. """

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return f"Error: El archivo '{file_path}' no se encontró."
    else:
        return content

# Pruebas
print(read_file('existing_file.txt'))  # Salida esperada: Contenido del archivo
print(read_file('non_existing_file.txt'))  # Salida esperada: Error: El archivo 'non_existing_file.txt' no se encontró.
print(read_file('another_missing_file.txt'))  # Salida esperada: Error: El archivo 'another_missing_file.txt' no se encontró.
print(read_file('existing_file.txt'))  # Salida esperada: Contenido del archivo
print(read_file('missing_file.txt'))  # Salida esperada: Error: El archivo 'missing_file.txt' no se encontró.