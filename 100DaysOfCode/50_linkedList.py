""" Día 50: Lista vinculada
Implementar una lista vinculada. """

class Node:
    """Clase que representa un nodo en una lista vinculada."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    """Clase que representa una lista vinculada."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Agrega un nuevo nodo con los datos dados al final de la lista."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        """Agrega un nuevo nodo con los datos dados al inicio de la lista."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        """Elimina el primer nodo que contiene los datos dados."""
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Mover head si es necesario
                    self.head = current.next
                return
            current = current.next

    def display(self):
        """Muestra los elementos de la lista."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def search(self, key):
        """Busca un nodo con los datos dados. Devuelve True si se encuentra, de lo contrario False."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
# Ejemplo de uso de la clase LinkedList
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    print("Lista después de agregar elementos:", ll.display())
    ll.delete(1)
    print("Lista después de eliminar el elemento 1:", ll.display())
    print("Buscar elemento 2 en la lista:", ll.search(2))
    print("Buscar elemento 3 en la lista:", ll.search(3))

# Salida esperada:
# Lista después de agregar elementos: [0, 1, 2]
# Lista después de eliminar el elemento 1: [0, 2]
# Buscar elemento 2 en la lista: True
# Buscar elemento 3 en la lista: False