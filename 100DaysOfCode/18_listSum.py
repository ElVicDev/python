""" Día 18: suma de la lista
Escriba una función para encontrar la suma de todos los elementos en una lista. """
def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = input("Ingrese una lista de números separados por comas: ")
number_list = [int(num) for num in numbers.split(",")]
print(f"La suma de la lista {number_list} es {list_sum(number_list)}.")
# Ejemplo de uso
# Ingrese una lista de números separados por comas: 1,2,3,4,5
# La suma de la lista [1, 2, 3, 4, 5] es 15.

# Ejemplo de uso
# Ingrese una lista de números separados por comas: 10,20,30
# La suma de la lista [10, 20, 30] es 60.

# Ejemplo de uso
# Ingrese una lista de números separados por comas: 5,10,15,20
# La suma de la lista [5, 10, 15, 20] es 50.