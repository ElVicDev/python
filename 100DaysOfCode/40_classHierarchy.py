""" Día 40: Jerarquía de clases
Cree una jerarquía de clase para diferentes formas (círculo, cuadrado, triángulo). """

import math

class Shape:
    """Clase base para todas las formas."""
    def area(self):
        raise NotImplementedError("El método area() debe ser implementado por la subclase.")

    def perimeter(self):
        raise NotImplementedError("El método perimeter() debe ser implementado por la subclase.")
    
class Circle(Shape):
    """Clase que representa un círculo."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calcula el área del círculo."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calcula el perímetro del círculo."""
        return 2 * math.pi * self.radius
    
class Square(Shape):
    """Clase que representa un cuadrado."""
    def __init__(self, side):
        self.side = side

    def area(self):
        """Calcula el área del cuadrado."""
        return self.side ** 2

    def perimeter(self):
        """Calcula el perímetro del cuadrado."""
        return 4 * self.side
    
class Triangle(Shape):
    """Clase que representa un triángulo."""
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """Calcula el área del triángulo usando la fórmula de Herón."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        """Calcula el perímetro del triángulo."""
        return self.side1 + self.side2 + self.side3
    
# Crear instancias de cada forma
shapes = [  Circle(5), Square(4), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"{shape.__class__.__name__} - Área: {shape.area():.2f}, Perímetro: {shape.perimeter():.2f}")

# Salida esperada:
# Circle - Área: 78.54, Perímetro: 31.42
# Square - Área: 16.00, Perímetro: 16.00
# Triangle - Área: 6.00, Perímetro: 12.00
