# try-except
""" Ejemplo de código que incorpora la estructura try-except para la 
    lectura de archivos """

file_name = "sample.txt"
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found -", file_name)