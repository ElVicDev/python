""" Día 67: Pandas
Cargue y manipule datos utilizando pandas. """

import pandas as pd

# Cargar datos desde un archivo CSV
data = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
print("Datos cargados:")
print(data.head())
# Manipular datos: Filtrar vuelos en enero
january_flights = data[data['JAN'] > 300]
print("\nVuelos en enero con más de 300 pasajeros:")
print(january_flights)
# Agregar una nueva columna: Total anual de pasajeros
data['Total'] = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].sum(axis=1)
print("\nDatos con columna Total anual:")
print(data)
# Guardar el DataFrame modificado a un nuevo archivo CSV
data.to_csv('modified_airtravel.csv', index=False)
print("\nDatos guardados en 'modified_airtravel.csv'")

# Output:
# Al ejecutar el script, se cargarán los datos del archivo CSV,
# se mostrarán los vuelos en enero con más de 300 pasajeros,
# se agregará una columna con el total anual de pasajeros,
# y se guardarán los datos modificados en un nuevo archivo CSV.

# Comparación con el código del día 66:
# El código del día 66 obtiene datos de una API externa
# y los muestra en una página web simple,
# mientras que este código del día 67 carga y manipula datos
# utilizando la biblioteca pandas.