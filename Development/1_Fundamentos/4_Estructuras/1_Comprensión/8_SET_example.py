""" Escribir el código Python necesario para tomar una lista de números 
    como entrada y devolver una nueva lista que contenga sólo los números 
    únicos de la lista original, manteniendo su orden original, 
    y luego imprimir el resultado. """

# Values provided (do not change)
array = [1, 2, 2, 3, 1, 4, 5, 3]

# The following line will need to change to only store unique values
unique_set = set()
# Inicializa una lista temporal para construir el resultado ordenado.
ordered_unique_list = []

# Iterar sobre el array original
for number in array:
    # Si el número no ha sido visto antes (es decir, es único en este punto)
    if number not in unique_set:
        # Añadir a la lista de resultados para mantener el orden
        ordered_unique_list.append(number)
        # Añadir al conjunto para marcarlo como 'visto'
        unique_set.add(number)

# La siguiente línea debe contener la lista ordenada (el resultado final)
unique_set = ordered_unique_list

# List conversion and print provided (do not change)
unique_array = list(unique_set)
print(unique_array)

""" Este código toma una lista de números con posibles duplicados,
    y utiliza un conjunto para rastrear los números únicos mientras
    mantiene el orden original en una lista separada.
    Finalmente, convierte la lista de números únicos en una lista
    y la imprime. """