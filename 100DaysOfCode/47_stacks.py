""" Día 47: Pilas
Implementar una estructura de datos de pila. """

class Stack:
    """Clase que representa una pila (LIFO - Last In, First Out)."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def push(self, item):
        """Agrega un elemento a la cima de la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento en la cima de la pila. Lanza una excepción si la pila está vacía."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Devuelve el elemento en la cima de la pila sin eliminarlo. Lanza una excepción si la pila está vacía."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.items)
    def display(self):
        """Muestra los elementos de la pila."""
        return self.items
    
# Ejemplo de uso de la clase Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushes:", stack.display())  # Muestra la pila después de agregar elementos
print("Top element (peek):", stack.peek())      # Muestra el elemento en la cima de la pila
print("Popped element:", stack.pop())            # Elimina y muestra el elemento en la
print("Stack after pop:", stack.display())       # Muestra la pila después de eliminar un elemento cima de la pila
print("Is stack empty?", stack.is_empty())       # Verifica si la pila está vacía
print("Stack size:", stack.size())               # Muestra el tamaño de la pila

# Salida esperada:
# Stack after pushes: [1, 2, 3]
# Top element (peek): 3
# Popped element: 3
# Stack after pop: [1, 2]
# Is stack empty? False
# Stack size: 2 cima de la pila