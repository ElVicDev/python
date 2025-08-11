""" Día 21: Lista inversa
Escriba una función para revertir una lista. """
def reverse_list(lst):
    if not lst:
        return []
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

numbers = input("Ingrese una lista de elementos separados por comas: ")
number_list = [item.strip() for item in numbers.split(",")]
print(f"La lista invertida de {number_list} es {reverse_list(number_list)}.")
# Ejemplo de uso
# Ingrese una lista de elementos separados por comas: 1,2,3,4,5
# La lista invertida de ['1', '2', '3', '4', '5'] es ['5', '4', '3', '2', '1'].

# Ejemplo de uso
# Ingrese una lista de elementos separados por comas: a,b,c,d,e
# La lista invertida de ['a', 'b', 'c', 'd', 'e'] es ['e', 'd', 'c', 'b', 'a'].

# Ejemplo de uso
# Ingrese una lista de elementos separados por comas: hola,mundo
# La lista invertida de ['hola', 'mundo'] es ['mundo', 'hola'].