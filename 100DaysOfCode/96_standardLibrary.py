""" Día 96: módulos de la biblioteca estándar de Python
Sumérgete en los módulos de la biblioteca estándar de Python 
(por ejemplo, datetime, itertools, functools). """

import datetime
import itertools
import functools
# Uso del módulo datetime para obtener la fecha y hora actuales
now = datetime.datetime.now()
print(f"Fecha y hora actuales: {now}")
# Uso del módulo itertools para crear un ciclo infinito
cycle = itertools.cycle(['A', 'B', 'C'])
print("Ciclo infinito de itertools (primeros 6 elementos):")
for _ in range(6):
    print(next(cycle), end=' ')
print()
# Uso del módulo functools para crear una función parcial
def multiply(x, y):
    return x * y
double = functools.partial(multiply, 2)
result = double(5)
print(f"Resultado de double(5): {result}")
""" Resultados esperados:
El programa imprimirá la fecha y hora actuales, los primeros seis elementos
de un ciclo infinito generado por itertools, y el resultado de la función
parcial que duplica un número. """
# Nota: Este código demuestra el uso de varios módulos de la biblioteca estándar
# de Python. Puede ejecutar este código en cualquier entorno Python sin necesidad
# de bibliotecas adicionales.