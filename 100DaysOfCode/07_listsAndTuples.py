""" Día 7: Listas y Tuples
Listas
Las listas son una de las estructuras de datos más utilizadas en Python. 
Están ordenados y mutables, lo que significa que puede cambiar su contenido 
después de la creación. 
Las listas pueden almacenar cualquier tipo de datos: 
cadenas, números o incluso otras listas. 
Esto los hace potentes y flexibles para una amplia gama de tareas.

Cree una lista: comience creando una lista con 5 elementos.
Estos podrían ser frutas, números o una combinación de tipos de datos.
Elementos de acceso: use índices positivos y negativos para recuperar 
elementos de la lista.
Modifique la lista: aprenda cómo agregar, insertar, eliminar o actualizar 
elementos utilizando métodos incorporados.
Corte la lista: use el corte para crear sublistas seleccionando un rango 
específico de elementos.
Iterar a través de la lista: use bucles (como para o mientras) para pasar 
por cada elemento y realizar operaciones en ellos.

Tuplas
Las tuplas también se ordenan colecciones, al igual que las listas, 
pero con una diferencia clave: son inmutables. 
Una vez que se crea una tupla, no puede cambiar su contenido. 
Las tuplas son ideales cuando desea almacenar datos que no deben modificarse, 
como coordenadas, configuraciones de configuración o valores fijos.

Cree una tupla: defina una tupla que contenga diferentes tipos de datos, 
como cadenas, números o booleanos.
Elementos de acceso: recupere elementos usando posiciones de índice, 
tal como lo haría con una lista.
Operaciones de tupla: Realice operaciones como Concatenation (+) y 
Repetition (*), o verifique la membresía con In.
Convierta a una lista: si necesita modificar la tupla, convertirla en una lista, 
realizar los cambios y convertirlo de nuevo si es necesario.
"""
# Listas
# Crear una lista con 5 elementos
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", fruits)
# Acceso a elementos
print("First element:", fruits[0])  # Acceso positivo
print("Last element:", fruits[-1])  # Acceso negativo
# Modificar la lista
fruits.append("fig")  # Agregar un elemento
print("After appending fig:", fruits)
fruits.insert(2, "grape")  # Insertar en una posición específica
print("After inserting grape at index 2:", fruits)
fruits.remove("banana")  # Eliminar un elemento
print("After removing banana:", fruits)
# Actualizar un elemento
fruits[1] = "blueberry"  # Actualizar el segundo elemento
print("After updating second element to blueberry:", fruits)
# Cortar la lista
sublist = fruits[1:4]  # Obtener elementos del índice 1 al 3
print("Sublist from index 1 to 3:", sublist)
# Iterar a través de la lista
print("Iterating through the list:")
for fruit in fruits:
    print(fruit)

# Tuplas
# Crear una tupla con diferentes tipos de datos
my_tuple = ("apple", 42, 3.14, True, "banana")
print("Original tuple:", my_tuple)
# Acceso a elementos
print("First element:", my_tuple[0])  # Acceso positivo
print("Last element:", my_tuple[-1])  # Acceso negativo
# Operaciones de tupla
print("Concatenated tuple:", my_tuple + ("cherry", "date"))  # Concatenación
print("Repeated tuple:", my_tuple * 2)  # Repetición
print("Is 'apple' in tuple?", "apple" in my_tuple)  # Verificar membresía
# Convertir a lista
my_list = list(my_tuple)  # Convertir tupla a lista
print("Converted to list:", my_list)
# Modificar la lista y convertir de nuevo a tupla
my_list.append("fig")  # Agregar un elemento
my_tuple = tuple(my_list)  # Convertir de nuevo a tupla
print("Modified tuple after converting back:", my_tuple)
print("End of Day 7 exercises.")
