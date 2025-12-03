# IndexError
""" Se produce cuando se intenta acceder a un elemento en un índice 
    que no existe dentro de esa secuencia. """

""" Causas:
    Acceso fuera de límites.
    Las secuencias están indexadas a cero en Python, lo que significa que 
    el primer elemento está en el índice 0. 
    Si se intenta acceder a un elemento en un índice mayor o igual que 
    la longitud de la secuencia, se producirá un error IndexError. 
    Por ejemplo, dada la lista my_list = [1, 2, 3], si se intenta acceder 
    a my_list[3] se producirá un error IndexError porque los índices válidos 
    son 0, 1 y 2.

    Secuencias vacías.
    Si se intenta acceder a cualquier índice de una lista, tupla o cadena vacía, 
    se producirá naturalmente un error. """

""" Soluciones:
    Compruebe la longitud de una secuencia antes de intentar acceder a sus elementos.
    Utilice un bucle que itere hasta la longitud de la secuencia, pero sin incluirla. """
my_list = [1, 2, 3]
for i in range(len(my_list)):
    print(my_list[i])

""" Si no está seguro de si una secuencia puede estar vacía, puede utilizar 
    una sentencia if para comprobar su longitud antes de continuar, o utilizar 
    un bloque try-except para capturar el IndexError y manejarlo con elegancia. """
my_list = []
try:
    print(my_list[0])
except IndexError:
    print("The list is empty.")