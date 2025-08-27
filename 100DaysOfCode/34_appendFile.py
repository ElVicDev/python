""" Día 34: Operaciones de archivo: Agregar
Agregar datos a un archivo de texto existente. """
with open("output.txt", "a") as file:
    file.write("This line is appended to the file.\n")
    file.write("Appending data helps in maintaining logs or records.\n")
print("Data appended to output.txt")