""" Comparación de la búsqueda en listas y diccionarios """

import timeit

# List lookup
list_data = list(range(100000))
lookup_value = 99999
list_time = timeit.timeit(lambda: lookup_value in list_data, number=1000)

# Dictionary lookup
dict_data = {i: i for i in range(100000)}
dict_time = timeit.timeit(lambda: lookup_value in dict_data, number=1000)

print("List lookup time:", list_time)
print("Dictionary lookup time:", dict_time)

""" La búsqueda por diccionario es significativamente más rápida que la búsqueda 
    por lista, especialmente para grandes conjuntos de datos """