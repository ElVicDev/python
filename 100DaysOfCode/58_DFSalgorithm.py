""" Día 58: Algoritmo de búsqueda de profundidad (DFS)
Implemente un algoritmo de búsqueda de profundidad (DFS). """

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("DFS starting from vertex A:")
dfs(graph, 'A')

# Output:
# DFS starting from vertex A:
# A B D E F C

# Comparación con el código del día 57:
# El código del día 57 implementa un algoritmo de búsqueda binaria,
# mientras que este código del día 58 implementa un algoritmo de búsqueda de profundidad (DFS).
# Ambos códigos tratan sobre algoritmos de búsqueda.