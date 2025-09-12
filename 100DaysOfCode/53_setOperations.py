""" Día 53: Operaciones establecidas
Realice varias operaciones en conjuntos (sindicato, intersección, etc.). """

class SetOperations:
    def __init__(self, initial_set=None):
        if initial_set is None:
            self.set = set()
        else:
            self.set = set(initial_set)

    def add(self, element):
        self.set.add(element)

    def remove(self, element):
        self.set.remove(element)

    def union(self, other_set):
        return self.set.union(other_set)

    def intersection(self, other_set):
        return self.set.intersection(other_set)

    def difference(self, other_set):
        return self.set.difference(other_set)

    def symmetric_difference(self, other_set):
        return self.set.symmetric_difference(other_set)

    def __str__(self):
        return str(self.set)
    
# Ejemplo de uso
set_ops = SetOperations([1, 2, 3])
set_ops.add(4)
print(set_ops)  # Output: {1, 2, 3, 4}
set_ops.remove(2)
print(set_ops)  # Output: {1, 3, 4}
other_set = {3, 4, 5}
print(set_ops.union(other_set))  # Output: {1, 3, 4, 5}
print(set_ops.intersection(other_set))  # Output: {3, 4}
print(set_ops.difference(other_set))  # Output: {1}
print(set_ops.symmetric_difference(other_set))  # Output: {1, 5}