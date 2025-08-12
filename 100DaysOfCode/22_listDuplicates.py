""" Día 22: Lista Duplicada
Escriba una función para eliminar los duplicados de una lista. """
def remove_duplicates(lst):
    if not lst:
        return []
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

elements = input("Ingrese una lista de elementos separados por comas: ")
element_list = [item.strip() for item in elements.split(",")]
print(f"La lista sin duplicados de {element_list} es {remove_duplicates(element_list)}.")
# Ejemplo de uso
# Ingrese una lista de elementos separados por comas: 1,2,2,3,4,4,5
# La lista sin duplicados de ['1', '2', '2', '3', '4', '4', '5'] es ['1', '2', '3', '4', '5'].

# Ejemplo de uso
# Ingrese una lista de elementos separados por comas: a,b,c,a,b,c
# La lista sin duplicados de ['a', 'b', 'c', 'a', 'b', 'c'] es ['a', 'b', 'c'].

# Ejemplo de uso
# Ingrese una lista de elementos separados por comas: hola,hola,mundo
# La lista sin duplicados de ['hola', 'hola', 'mundo'] es ['hola', 'mundo'].