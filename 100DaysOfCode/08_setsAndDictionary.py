""" Día 8: Sets and Dictionary
Sets
Los conjuntos son colecciones desordenadas de elementos únicos. 
Son útiles cuando desea eliminar los duplicados y realizar operaciones 
establecidas comunes como unión, intersección y diferencia. 
Dado que los conjuntos están desordenados, los elementos no tienen una 
posición fija y no se puede acceder utilizando un índice.

Cree un conjunto: 
Defina un conjunto con múltiples elementos, incluidos los duplicados, 
y observe cómo se eliminan automáticamente los duplicados.
Agregue y elimine los elementos: 
Use add() para insertar elementos y discard() o remove() para eliminarlos.
Operaciones establecidas: 
Aprenda a realizar operaciones de conjunto matemático como union(), 
intersection() y difference().
Reunir a través de un conjunto:
Use un bucle para iterar sobre los elementos en un conjunto.

Diccionario
Los diccionarios son colecciones desordenadas de pares de valor clave. 
Le permiten asociar una clave única con un valor, lo que los hace ideales 
para buscar datos de manera eficiente. 
Las teclas deben ser únicas e inmutables, mientras que los valores pueden 
ser de cualquier tipo.

Cree un diccionario: 
Defina un diccionario con claves y valores correspondientes (por ejemplo, 
pares de nombre de edad).
Valores de acceso: 
Use una clave para recuperar el valor asociado usando corchetes o 
el método get ().
Actualice y agregue elementos: 
modifique los pares de valor clave existentes o agregue otros nuevos.
Eliminar elementos: 
Use métodos como pop () o Del para eliminar las entradas del diccionario.
Luce a través de un diccionario: 
Iterar a través de claves, valores o ambos usando un bucle 
para .items(), .keys() o .values().
"""

# Sets
# Crear un conjunto con elementos duplicados
my_set = {1, 2, 3, 4, 4, 5}  # Los duplicados se eliminan automáticamente
print("Original set:", my_set)
# Agregar y eliminar elementos
my_set.add(6)  # Agregar un elemento
print("After adding 6:", my_set)
my_set.discard(2)  # Eliminar un elemento (no genera error si no existe)
print("After discarding 2:", my_set)
my_set.remove(3)  # Eliminar un elemento (genera error si no existe)
print("After removing 3:", my_set)
# Operaciones de conjunto
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Set A:", set_a)
print("Set B:", set_b)
print("Union of A and B:", set_a.union(set_b))  # Unión
print("Intersection of A and B:", set_a.intersection(set_b))  # Intersección
print("Difference of A and B:", set_a.difference(set_b))  # Diferencia
# Iterar a través de un conjunto
print("Iterating through the set:")
for item in my_set:
    print(item)
# Acceso a elementos
# No se puede acceder a los elementos de un conjunto por índice,
# ya que son desordenados, pero se pueden iterar o convertir a una lista
# Acceso a elementos
my_set_list = list(my_set)  # Convertir a lista para acceder por índice 
print("First element in set as list:", my_set_list[0])  # Acceso positivo
# Acceso a elementos
print("Last element in set as list:", my_set_list[-1])  # Acceso negativo

# Dictionary
# Crear un diccionario con claves y valores
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Original dictionary:", my_dict)
# Acceso a valores
print("Name:", my_dict["name"])  # Acceso usando clave
print("Age:", my_dict.get("age"))  # Acceso usando el método get()
# Actualizar y agregar elementos
my_dict["age"] = 31  # Actualizar un valor existente
print("After updating age:", my_dict)
my_dict["country"] = "USA"  # Agregar un nuevo par clave-valor
print("After adding country:", my_dict)
# Eliminar elementos
my_dict.pop("city")  # Eliminar un elemento usando pop()
print("After popping city:", my_dict)
del my_dict["name"]  # Eliminar un elemento usando del
print("After deleting name:", my_dict)
# Iterar a través de un diccionario
print("Iterating through the dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
