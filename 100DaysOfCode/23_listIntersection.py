""" Día 23: Intersección de la lista
Escriba una función para encontrar la intersección de dos listas. """

def list_intersection(lst1, lst2):
    if not lst1 or not lst2:
        return []
    intersection = []
    for item in lst1:
        if item in lst2 and item not in intersection:
            intersection.append(item)
    return intersection

list1 = input("Ingrese la primera lista de elementos separados por comas: ")
list2 = input("Ingrese la segunda lista de elementos separados por comas: ")
list1 = [item.strip() for item in list1.split(",")]
list2 = [item.strip() for item in list2.split(",")]
print(f"La intersección de {list1} y {list2} es {list_intersection(list1, list2)}.")
# Ejemplo de uso
# Ingrese la primera lista de elementos separados por comas: 1,2,3,4
# Ingrese la segunda lista de elementos separados por comas: 3,4,5,6
# La intersección de ['1', '2', '3', '4'] y ['3', '4', '5', '6'] es ['3', '4'].
# Ejemplo de uso
# Ingrese la primera lista de elementos separados por comas: a,b,c
# Ingrese la segunda lista de elementos separados por comas: b,c,d
# La intersección de ['a', 'b', 'c'] y ['b', 'c', 'd'] es ['b', 'c'].
# Ejemplo de uso
# Ingrese la primera lista de elementos separados por comas: hola,mundo
# Ingrese la segunda lista de elementos separados por comas: mundo,python
# La intersección de ['hola', 'mundo'] y ['mundo', 'python'] es ['mundo'].