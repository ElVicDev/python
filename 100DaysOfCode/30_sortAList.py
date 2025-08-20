""" Día 30: Ordene una lista
Ordene una lista de números en orden ascendente. """

def sort_list(numbers):
    return sorted(numbers)
numbers_input = input("Ingrese una lista de números separados por espacios: ")
numbers = list(map(int, numbers_input.split()))
sorted_numbers = sort_list(numbers)
print("Lista ordenada:", sorted_numbers)

# Ejemplo de uso
# Ingrese una lista de números separados por espacios: 34 2 23 67 4
# Lista ordenada: [2, 4, 23, 34, 67]

# Ejemplo de uso
# Ingrese una lista de números separados por espacios: 5 3 8 1 2
# Lista ordenada: [1, 2, 3, 5, 8]

# Ejemplo de uso
# Ingrese una lista de números separados por espacios: 10 20 5 15
# Lista ordenada: [5, 10, 15, 20]