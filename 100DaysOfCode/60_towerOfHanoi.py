""" Día 60: Torre de Hanoi
Resuelve el problema de la Torre de Hanoi. """

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Mover disco 1 de {source} a {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Mover disco {n} de {source} a {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Ejemplo de uso
n = 3  # Número de discos
print(f"Solución para {n} discos:")
tower_of_hanoi(n, 'A', 'C', 'B')

# Output:
# Solución para 3 discos:
# Mover disco 1 de A a C
# Mover disco 2 de A a B
# Mover disco 1 de C a B
# Mover disco 3 de A a C
# Mover disco 1 de B a A
# Mover disco 2 de B a C
# Mover disco 1 de A a C

# Comparación con el código del día 59:
# El código del día 59 implementa un algoritmo de búsqueda en anchura (BFS),
# mientras que este código del día 60 resuelve el problema de la Torre de Hanoi.
# Ambos códigos tratan sobre algoritmos recursivos,
# pero abordan diferentes problemas: uno se centra en la búsqueda en grafos
# mientras que el otro se centra en la manipulación y ordenación de datos.