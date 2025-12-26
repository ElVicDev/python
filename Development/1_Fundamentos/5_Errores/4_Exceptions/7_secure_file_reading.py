""" Escriba una función Python llamada read_file_contents que tome file_path 
    como argumento.
    Dentro de la función, utilice un bloque try-except para intentar abrir el 
    archivo, leer su contenido e imprimirlo en la consola.
    Maneje el FileNotFoundError específicamente imprimiendo un mensaje de error 
    apropiado si el archivo no existe.

Consejos:
    Nombre su variable de archivo file.
    Usa la sentencia with open(), que asegura que el archivo se cierra 
    automáticamente, por lo que llamar a file.close() en el bloque finally 
    no será necesario.

Ejemplo Entrada:
    read_file_contents("/Users/Example/Documents/my_file.txt")

Salida esperada:
    Error: Archivo no encontrado - /Usuarios/Ejemplo/Documentos/mi_archivo.txt """

def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado - {file_path}")

# Ejemplo de uso
read_file_contents("/Users/Example/Documents/my_file.txt")