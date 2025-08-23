""" Día 32: Operaciones de archivo: leer
Lea y muestre el contenido de un archivo de texto. """

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: El archivo no se encontró."
file_path = input("Ingrese la ruta del archivo de texto: ")
file_content = read_file(file_path)
print("Contenido del archivo:\n", file_content)

# Ejemplo de uso
# Ingrese la ruta del archivo de texto: ejemplo.txt
# Contenido del archivo:
# Este es un archivo de ejemplo.