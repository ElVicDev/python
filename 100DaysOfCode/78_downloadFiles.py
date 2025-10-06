""" Día 78: Descargar archivos
Cree un script para descargar archivos de un sitio web. """

import requests
import os

# Función para descargar un archivo desde una URL
def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica que la solicitud fue exitosa
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Archivo descargado y guardado en: {save_path}")
    except Exception as e:
        print(f"Ocurrió un error al descargar el archivo: {e}")

# Especificar la URL del archivo y la ruta donde se guardará
file_url = "https://www.gutenberg.org/cache/epub/64058/pg64058.txt"  # Cambie esto a la URL del archivo que desea descargar
save_directory = "./downloads"  # Cambie esto al directorio donde desea guardar el archivo
os.makedirs(save_directory, exist_ok=True)
file_name = os.path.join(save_directory, "LaTiaTula.txt")  # Cambie esto al nombre con el que desea guardar el archivo

# Llamar a la función para descargar el archivo
download_file(file_url, file_name)

# Output:
# Al ejecutar el script, el archivo desde la URL especificada
# será descargado y guardado en el directorio especificado.
# Asegúrese de que la URL sea válida y que el directorio 
# "./downloads" exista o se cree automáticamente.