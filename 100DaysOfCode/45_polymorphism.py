""" Día 45: Polimorfismo
Implementar polimorfismo con una calculadora de área de forma. """

import math
class Shape:
    """Clase base para diferentes formas geométricas."""
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Circle(Shape):
    """Clase que representa un círculo."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calcula el área del círculo."""
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    """Clase que representa un rectángulo."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height
    
# Función para calcular el área de cualquier forma
def calculate_area(shape):
    return shape.area()

# Crear instancias de Circle y Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Area of Circle: {calculate_area(circle):.2f}")      # Área del círculo
print(f"Area of Rectangle: {calculate_area(rectangle):.2f}")  # Área del rectángulo

# Salida esperada:
# Area of Circle: 78.54
# Area of Rectangle: 24.00
