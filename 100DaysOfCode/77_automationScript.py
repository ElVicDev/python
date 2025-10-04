""" Día 77: Script de automatización
Escriba un script para automatizar el cambio de nombre de archivos. """

import os
import shutil
# Función para cambiar el nombre de archivos en un directorio
def rename_files_in_directory(directory, prefix):
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                new_name = f"{prefix}_{filename}"
                shutil.move(os.path.join(directory, filename), os.path.join(directory, new_name))
                print(f"Renombrado: {filename} a {new_name}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
# Especificar el directorio y el prefijo
directory_path = "./test_directory"  # Cambie esto al directorio que desea usar
prefix = "renombrado"
# Llamar a la función para renombrar archivos
rename_files_in_directory(directory_path, prefix)
# Output:
# Al ejecutar el script, todos los archivos en el directorio especificado
# serán renombrados con el prefijo dado.
# Asegúrese de que el directorio "./test_directory" exista y contenga archivos para ver el efecto.