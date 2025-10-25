"""  Este módulo llamado geometry_calculations.py, incluye:
    Import: 
    Una sentencia para importar el módulo math, que proporciona 
    constantes matemáticas como pi y funciones matemáticas como sqrt.
    Funciones:
    Dos funciones (calculate_area_circle y calculate_circumference_circle)
    para calcular el área y la circunferencia de círculos.
    Clase:
    Una clase llamada Rectangle que representa un rectángulo y tiene 
    métodos para calcular su área y perímetro.
Cada componente de este módulo tiene un propósito específico relacionado 
con los cálculos geométricos. """

import math

def calculate_area_circle(radius):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radius**2

def calculate_circumference_circle(radius):
    """Calcula la circunferencia de un círculo dado su radio."""
    return 2 * math.pi * radius

class Rectangle:
    """Representa un rectángulo con ancho y alto."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def calculate_perimeter(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)