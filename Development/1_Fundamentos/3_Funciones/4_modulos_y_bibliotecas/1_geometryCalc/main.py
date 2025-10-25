""" Para aprovechar las capacidades del módulo geometry_calculations.py
    importarlo a este archivo Python main.py. """

import geometry_calculations

radius = 5
area = geometry_calculations.calculate_area_circle(radius)
circumference = geometry_calculations.calculate_circumference_circle(radius)

print(f"Area of circle: {area}")
print(f"Circumference of circle: {circumference}")

rect = geometry_calculations.Rectangle(4, 6)
rect_area = rect.calculate_area()
rect_perimeter = rect.calculate_perimeter()

print(f"Area of rectangle: {rect_area}")
print(f"Perimeter of rectangle: {rect_perimeter}")

""" En el archivo main.py, iniciamos el proceso importando nuestro 
    módulo geometry_calculations. 
    A continuación, definimos el radio de un círculo (radius) y utilizamos 
    las funciones del módulo para calcular e imprimir su área y circunferencia. 
    Además, creamos un objeto Rectangle utilizando la clase del módulo, 
    y luego calculamos e imprimimos su área y perímetro. """

""" Resultados esperados:
Area of circle: 78.53981633974483
Circumference of circle: 31.41592653589793
Area of rectangle: 24
Perimeter of rectangle: 20 """