""" Día 68: Matplotlib
Cree visualizaciones de datos utilizando matplotlib. """

import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde un archivo CSV
data = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
# Agregar una nueva columna: Total anual de pasajeros
data['Total'] = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].sum(axis=1)
print("Datos cargados:")
print(data.head())
# Crear una visualización: Gráfico de barras del total anual de pasajeros por mes
plt.figure(figsize=(10, 6))
plt.bar(data['Month'], data['Total'], color='skyblue')
plt.title('Total Anual de Pasajeros por Mes')
plt.xlabel('Mes')
plt.ylabel('Total de Pasajeros')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('annual_passengers.png')
plt.show()
print("\nGráfico guardado como 'annual_passengers.png'")

# Output:
# Al ejecutar el script, se cargarán los datos del archivo CSV,
# se mostrará una vista previa de los datos,
# y se generará un gráfico de barras que se guardará como 'annual_passengers.png
# y se mostrará en pantalla.

# Comparación con el código del día 67:
# El código del día 67 carga y manipula datos utilizando pandas,
# mientras que este código del día 68 también crea una visualización
# de esos datos utilizando matplotlib.