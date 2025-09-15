""" Día 56: Algoritmos de clasificación
Implementar algoritmos de clasificación 
(por ejemplo, clasificación de burbujas, clasificación de fusión). """

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Ejemplo de uso
array1 = [64, 34, 25, 12, 22, 11, 90]
sorted_array1 = bubble_sort(array1.copy())
print("Sorted array using Bubble Sort:", sorted_array1)
array2 = [38, 27, 43, 3, 9, 82, 10]
sorted_array2 = merge_sort(array2.copy())
print("Sorted array using Merge Sort:", sorted_array2)

# Output:
# Sorted array using Bubble Sort: [11, 12, 22, 25, 34, 64, 90]
# Sorted array using Merge Sort: [3, 9, 10, 27, 38, 43, 82]

# Comparación con el código del día 55:
# El código del día 55 implementa una clase iterable personalizada, 
# mientras que este código del día 56 implementa dos algoritmos de 
# clasificación: bubble sort y merge sort. 
# Ambos códigos demuestran conceptos fundamentales de programación, 
# pero en áreas diferentes: uno en la creación de clases e iteradores, 
# y el otro en algoritmos y manipulación de listas.
# Ambos códigos incluyen ejemplos de uso y muestran cómo funcionan 
# las implementaciones.