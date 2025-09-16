""" Día 59: Algoritmo de búsqueda de la primera búsqueda (BFS)
Implemente un algoritmo de búsqueda de la primera búsqueda (BFS). """

from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
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
print("BFS starting from vertex A:")
bfs(graph, 'A')

# Output:
# BFS starting from vertex A:
# A B C D E F

# Comparación con el código del día 58:
# El código del día 58 implementa un algoritmo de búsqueda en profundidad (DFS),
# mientras que este código del día 59 implementa un algoritmo de búsqueda en anchura (BFS).
# Ambos códigos tratan sobre algoritmos de búsqueda,
# pero abordan diferentes aspectos: uno se centra en la profundidad
# mientras que el otro se centra en la anchura.