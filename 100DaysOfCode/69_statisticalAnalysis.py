""" Día 69: Análisis estadístico
Realice un análisis estadístico en un conjunto de datos. """

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
# Cargar datos desde un archivo CSV
data = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
# Agregar una nueva columna: Total anual de pasajeros
data['Total'] = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].sum(axis=1)
print("Datos cargados:")
print(data.head())
# Análisis estadístico
mean_total = np.mean(data['Total'])
median_total = np.median(data['Total'])
mode_total = stats.mode(data['Total'])[0][0]
std_dev_total = np.std(data['Total'])
print(f"\nAnálisis Estadístico del Total Anual de Pasajeros:")
print(f"Media: {mean_total}")
print(f"Mediana: {median_total}")
print(f"Moda: {mode_total}")
print(f"Desviación Estándar: {std_dev_total}")
# Visualización del análisis estadístico
plt.figure(figsize=(10, 6))
sns.histplot(data['Total'], bins=10, kde=True, color='skyblue')
plt.axvline(mean_total, color='red', linestyle='dashed', linewidth=1, label='Media')
plt.axvline(median_total, color='green', linestyle='dashed', linewidth=1, label='Mediana')
plt.axvline(mode_total, color='orange', linestyle='dashed', linewidth=1, label='Moda')
plt.title('Distribución del Total Anual de Pasajeros')
plt.xlabel('Total de Pasajeros')
plt.ylabel('Frecuencia')
plt.legend()
plt.tight_layout()
plt.savefig('statistical_analysis.png')
plt.show()
print("\nGráfico guardado como 'statistical_analysis.png'")

# Output:
# Al ejecutar el script, se cargarán los datos del archivo CSV,
# se mostrará una vista previa de los datos,
# se realizará un análisis estadístico del total anual de pasajeros,
# y se generará un histograma que se guardará como 'statistical_analysis.png'
# y se mostrará en pantalla.

# Comparación con el código del día 68:
# El código del día 68 crea una visualización de los datos utilizando matplotlib,
# mientras que este código del día 69 realiza un análisis estadístico
# y crea una visualización adicional para mostrar la distribución de los datos.