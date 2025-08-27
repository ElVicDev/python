""" Día 33: Operaciones de archivo: escribir
Escriba datos en un archivo de texto. """
with open("output.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Writing data to files is essential for data persistence.\n")
    file.write("This is the third line in the file.\n")
    file.write("End of the file.\n")

print("Data written to output.txt")