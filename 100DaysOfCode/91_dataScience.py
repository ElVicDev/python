""" Día 91: Ciencia de datos
Utilice Python para proyectos de ciencia de datos 
(por ejemplo, limpieza de datos, ingeniería de funciones). """

import pandas as pd
import numpy as np
def clean_data(df):
    """Función para limpiar datos eliminando valores nulos y duplicados."""
    df = df.dropna()  # Eliminar filas con valores nulos
    df = df.drop_duplicates()  # Eliminar filas duplicadas
    return df
def engineer_features(df):
    """Función para crear nuevas características a partir de las existentes."""
    df['feature_sum'] = df.sum(axis=1)  # Suma de todas las columnas por fila
    df['feature_mean'] = df.mean(axis=1)  # Media de todas las columnas por fila
    return df
if __name__ == "__main__":
    # Crear un DataFrame de ejemplo con datos sucios
    data = {
        'A': [1, 2, np.nan, 4, 5, 5],
        'B': [5, np.nan, np.nan, 8, 10, 10],
        'C': [9, 8, 7, 6, 5, 5]
    }
    df = pd.DataFrame(data)
    print("Datos originales:")
    print(df)
    # Limpiar los datos
    cleaned_df = clean_data(df)
    print("\nDatos limpios:")
    print(cleaned_df)
    # Ingeniería de características
    featured_df = engineer_features(cleaned_df)
    print("\nDatos con características nuevas:")
    print(featured_df)
""" Resultados esperados:
El programa imprimirá el DataFrame original con datos sucios, el DataFrame limpio sin valores nulos ni duplicados, y el DataFrame final con nuevas características añadidas.
"""
# Nota: Asegúrese de tener las bibliotecas pandas y numpy instaladas en su sistema para ejecutar este código.
# Puede instalar estas bibliotecas utilizando pip:
# pip install pandas numpy
# Este código crea un DataFrame de ejemplo, limpia los datos eliminando valores nulos y
# duplicados, y luego añade nuevas características basadas en las columnas existentes.
# Puede modificar el DataFrame de ejemplo o cargar sus propios datos para experimentar
# con la limpieza de datos y la ingeniería de características.
# Asegúrese de ejecutar este código en un entorno adecuado que soporte pandas y numpy,
# como una terminal o un IDE.
# Este ejemplo es básico y puede necesitar ajustes según sus necesidades específicas.
# Para proyectos de ciencia de datos más complejos, considere explorar bibliotecas
# adicionales como scikit-learn para modelado y análisis avanzado.
# Además, para conjuntos de datos grandes, considere optimizaciones adicionales
# como el uso de Dask para manejar datos que no caben en memoria.
# El código anterior demuestra técnicas básicas de limpieza de datos
# e ingeniería de características utilizando pandas y numpy.