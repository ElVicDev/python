""" Día 49: Árbol de búsqueda binario
Implementar un árbol de búsqueda binario. """

class TreeNode:
    """Clase que representa un nodo en un árbol de búsqueda binario."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    """Clase que representa un árbol de búsqueda binario."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserta un nuevo nodo con la clave dada en el árbol."""
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        """Método recursivo para insertar un nuevo nodo."""
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def search(self, key):
        """Busca un nodo con la clave dada en el árbol. Devuelve True si se encuentra, de lo contrario False."""
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        """Método recursivo para buscar un nodo."""
        if node is None:
            return False
        if node.val == key:
            return True
        elif key < node.val:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)

    def inorder_traversal(self):
        """Realiza un recorrido inorden del árbol y devuelve una lista de los valores."""
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, node, result):
        """Método recursivo para el recorrido inorden."""
        if node:
            self._inorder_rec(node.left, result)
            result.append(node.val)
            self._inorder_rec(node.right, result)

# Ejemplo de uso de la clase BinarySearchTree
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)
print("Inorder traversal:", bst.inorder_traversal())  # Muestra el recorrido inorden del árbol
print("Search for 4:", bst.search(4))                 # Busca el valor 4
print("Search for 10:", bst.search(10))               # Busca el valor 10

# Salida esperada:
# Inorder traversal: [2, 3, 4, 5, 6, 7, 8]
# Search for 4: True
# Search for 10: False