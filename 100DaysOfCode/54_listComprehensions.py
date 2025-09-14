""" Día 54: Comprensiones de la lista
Use las comprensiones de la lista para filtrar y transformar listas. """

class ListComprehensions:
    def __init__(self, initial_list=None):
        if initial_list is None:
            self.list = []
        else:
            self.list = list(initial_list)

    def add(self, element):
        self.list.append(element)

    def filter_even(self):
        return [x for x in self.list if x % 2 == 0]

    def square(self):
        return [x**2 for x in self.list]

    def filter_greater_than(self, threshold):
        return [x for x in self.list if x > threshold]

    def __str__(self):
        return str(self.list)
    
# Ejemplo de uso
list_comp = ListComprehensions([1, 2, 3, 4, 5])
list_comp.add(6)
print(list_comp)  # Output: [1, 2, 3, 4, 5, 6]
print(list_comp.filter_even())  # Output: [2, 4, 6]
print(list_comp.square())  # Output: [1, 4, 9, 16, 25, 36]
print(list_comp.filter_greater_than(3))  # Output: [4, 5, 6]