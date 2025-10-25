""" Definimos una función llamada calculate_mean 
    que aprovecha la biblioteca NumPy (np) para calcular la media de una 
    lista de números.
    Importamos este módulo y utilizaríamos la función 
    de la siguiente manera:  """

import data_analysis_tools

my_data = [2, 4, 5, 8, 1, 9]
mean_value = data_analysis_tools.calculate_mean(my_data)
print(f"Mean: {mean_value}")

""" En este ejemplo, importamos el módulo data_analysis_tools y luego 
    definimos una lista de números (my_data).
    Usamos la función calculate_mean del módulo para calcular la media
    de los números en la lista e imprimimos el resultado. """
""" Resultados esperados:
Mean: 4.833333333333333 """