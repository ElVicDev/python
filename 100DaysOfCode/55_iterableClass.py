""" Día 55: Clase Iterable.
Implementar una clase ITerable personalizada. """

class IterableClass:
    def __init__(self, initial_list=None):
        if initial_list is None:
            self.list = []
        else:
            self.list = list(initial_list)
        self.index = 0

    def add(self, element):
        self.list.append(element)

    def __iter__(self):
        self.index = 0  # Reiniciar el índice para una nueva iteración
        return self

    def __next__(self):
        if self.index < len(self.list):
            result = self.list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        return str(self.list)
    
# Ejemplo de uso
iterable = IterableClass([1, 2, 3])
iterable.add(4)
print(iterable)  # Output: [1, 2, 3, 4]
for item in iterable:
    print(item)  # Output: 1 2 3 4 (cada número en una línea)
# Reiniciar la iteración
for item in iterable:
    print(item)  # Output: 1 2 3 4 (cada número en una línea)