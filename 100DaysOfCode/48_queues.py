""" Día 48: colas
Implementar una estructura de datos de cola. """

class Queue:
    """Clase que representa una cola (FIFO - First In, First Out)."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Agrega un elemento al final de la cola."""
        self.items.append(item)

    def dequeue(self):
        """Elimina y devuelve el elemento al frente de la cola. Lanza una excepción si la cola está vacía."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        """Devuelve el elemento al frente de la cola sin eliminarlo. Lanza una excepción si la cola está vacía."""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]

    def size(self):
        """Devuelve el número de elementos en la cola."""
        return len(self.items)
    
    def display(self):
        """Muestra los elementos de la cola."""
        return self.items
    
# Ejemplo de uso de la clase Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue.display())  # Muestra la cola después de agregar
print("Front element:", queue.front())            # Muestra el elemento al frente de la cola
print("Dequeued element:", queue.dequeue())       # Elimina y muestra el elemento al frente
print("Queue after dequeue:", queue.display())     # Muestra la cola después de eliminar un elemento
print("Is queue empty?", queue.is_empty())        # Verifica si la cola está vac
print("Queue size:", queue.size())                # Muestra el tamaño de la cola

# Salida esperada:
# Queue after enqueues: [1, 2, 3]
# Front element: 1
# Dequeued element: 1
# Queue after dequeue: [2, 3]
# Is queue empty? False
# Queue size: 2