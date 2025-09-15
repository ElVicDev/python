""" Día 57: Algoritmos de búsqueda
Implementar algoritmos de búsqueda (por ejemplo, búsqueda binaria). """

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Ejemplo de uso
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pero abordan diferentes aspectos: uno se centra en la iteración
index = binary_search(sorted_array, 7)
print("Element found at index:", index)  # Output: Element found at index: 6 
# mientras que el otro se centra en la manipulación y ordenación de datos.
index = binary_search(sorted_array, 11)
print("Element found at index:", index)  # Output: Element found at index: -1

# Output:
# Element found at index: 6
# Element found at index: -1

# Comparación con el código del día 56:
# El código del día 56 implementa dos algoritmos de clasificación 
# (bubble sort y merge sort), mientras que este código del día 57 
# implementa un algoritmo de búsqueda (búsqueda binaria).