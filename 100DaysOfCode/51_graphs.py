""" Día 51: Gráficos
Implementar una estructura de datos de gráficos. """

class Graph:
    """Clase que representa un gráfico utilizando una lista de adyacencia."""
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Agrega una arista entre los nodos u y v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Para gráficos no dirigidos

    def remove_edge(self, u, v):
        """Elimina la arista entre los nodos u y v."""
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def display(self):
        """Muestra el gráfico como una lista de adyacencia."""
        return self.graph

    def bfs(self, start):
        """Realiza una búsqueda en anchura (BFS) desde el nodo de inicio."""
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend([neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited])
        
        return result

    def dfs(self, start):
        """Realiza una búsqueda en profundidad (DFS) desde el nodo de inicio."""
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                stack.extend([neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited])
        
        return result