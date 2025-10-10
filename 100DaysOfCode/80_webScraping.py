""" Día 80: raspado web
Escriba un script para extraer datos de un sitio web. """

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.figure_factory as ff
import plotly.subplots as sp
import plotly.offline as pyo
import plotly.colors as pc

# URL del sitio web a raspar
url = 'https://www.iana.org/domains/reserved'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# Encuentra la tabla en la página web
table = soup.find('table')
# Extrae los encabezados de la tabla
headers = [header.text for header in table.find_all('th')]
# Extrae las filas de la tabla
rows = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    rows.append([cell.text for cell in cells])
# Crea un DataFrame de pandas
df = pd.DataFrame(rows, columns=headers)
# Limpia los datos (convierte tipos de datos, maneja valores faltantes, etc.)
df.replace('', np.nan, inplace=True)
df.dropna(inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(lambda x: re.sub(r'[^\d.]', '', x)).astype(float)
# Análisis de datos
summary = df.describe()
correlation = df.corr()
# Visualización de datos
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Mapa de calor de correlación')
plt.show()
# Gráfico interactivo con Plotly
fig = px.scatter_matrix(df, dimensions=df.columns, title='Matriz de dispersión interactiva')
fig.show()
# Guardar el DataFrame limpio en un archivo CSV
df.to_csv('cleaned_data.csv', index=False)
# Guardar el resumen estadístico en un archivo CSV
summary.to_csv('data_summary.csv')
# Guardar la matriz de correlación en un archivo CSV
correlation.to_csv('data_correlation.csv')
print("Datos raspados y analizados con éxito.")
# Nota: Asegúrese de cambiar 'https://example.com/data' a la URL real del sitio web que desea raspar.
# Además, instale las bibliotecas necesarias si aún no lo ha hecho:
# pip install requests beautifulsoup4 pandas matplotlib seaborn plotly
# Tenga en cuenta las políticas de raspado del sitio web y respete los términos de servicio.
# Este es un ejemplo básico y puede necesitar ajustes según la estructura específica del sitio web que está raspando.
# Además, considere manejar excepciones y errores para hacer el script más robusto.