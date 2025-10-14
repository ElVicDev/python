""" Día 87: rastreador web
Cree un rastreador web o un raspador web. """

import requests
from bs4 import BeautifulSoup
# URL de la página web que desea rastrear
url = 'https://example.com'
# Realizar una solicitud GET a la página web
response = requests.get(url)
# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página web
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encontrar todos los enlaces en la página
    links = soup.find_all('a')
    print(f"Found {len(links)} links on the page:")
    for link in links:
        href = link.get('href')
        text = link.text.strip()
        print(f"Link text: {text}, URL: {href}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
""" Resultados esperados:
El programa imprimirá el número de enlaces encontrados en la página web
y mostrará el texto y la URL de cada enlace.
"""
# Nota: Asegúrese de tener las bibliotecas necesarias instaladas:
# pip install requests beautifulsoup4
# Además, respete los términos de servicio del sitio web que está rastreando.
# Algunos sitios web pueden tener medidas para bloquear rastreadores web.
# Siempre verifique el archivo robots.txt del sitio web para ver qué está permitido rastrear.
# Este código es un ejemplo básico y puede necesitar ajustes según la estructura
# específica del sitio web que está rastreando.
# Además, para un rastreador web más avanzado, considere manejar paginación,
# seguir enlaces internos, y almacenar los datos recopilados en una base de datos o archivo.
# Tenga en cuenta que el rastreo web puede tener implicaciones legales y éticas.
# Asegúrese de cumplir con las leyes y regulaciones aplicables en su jurisdicción
# y de respetar la privacidad y los derechos de los propietarios del sitio web.
# Siempre consulte con un asesor legal si no está seguro sobre las prácticas de rastreo web.
# El código anterior realiza una solicitud a una página web, analiza su contenido HTML
# y extrae todos los enlaces presentes en la página, mostrando su texto y URL.
# Asegúrese de ejecutar este código en un entorno adecuado con acceso a Internet.
# Cambie 'https://example.com' a la URL del sitio web que desea rastrear.
# El código anterior es un ejemplo básico de un rastreador web.
# Para un rastreador web más avanzado, considere manejar paginación.
