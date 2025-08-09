""" Día 19: máximo en la lista
Escriba una función para encontrar el elemento máximo en una lista. """
def list_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

numbers = input("Ingrese una lista de números separados por comas: ")
number_list = [int(num) for num in numbers.split(",")]
print(f"El máximo de la lista {number_list} es {list_max(number_list)}.")
# Ejemplo de uso
# Ingrese una lista de números separados por comas: 1,2,3,4,5
# El máximo de la lista [1, 2, 3, 4, 5] es 5.
# Ejemplo de uso
# Ingrese una lista de números separados por comas: 10,20,30
# El máximo de la lista [10, 20, 30] es 30.
# Ejemplo de uso
# Ingrese una lista de números separados por comas: 5,10,15,20
# El máximo de la lista [5, 10, 15, 20] es 20.