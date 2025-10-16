""" Día 89: Generar fractales
Escribe un programa para generar fractales. """

import matplotlib.pyplot as plt
import numpy as np
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n
def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height, max_iter = 800, 800, 100
r1, r2, fractal = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
plt.imshow(fractal, extent=(xmin, xmax, ymin, ymax), cmap='hot')
plt.colorbar()
plt.title('Conjunto de Mandelbrot')
plt.show()

""" Resultados esperados:
El programa generará y mostrará una imagen del conjunto de Mandelbrot.
"""
# Nota: Asegúrese de tener las bibliotecas necesarias instaladas:
# pip install matplotlib numpy
# El código anterior genera una imagen del conjunto de Mandelbrot,
# que es un tipo de fractal. Puede ajustar los parámetros xmin, xmax, ymin, ymax,
# width, height y max_iter para explorar diferentes partes del fractal y niveles de detalle.
# Asegúrese de ejecutar este código en un entorno adecuado con soporte para gráficos,
# como Jupyter Notebook, o un entorno de desarrollo integrado (IDE) que soporte la visual
# ización de gráficos.ización de gráficos.
# El conjunto de Mandelbrot es solo uno de los muchos tipos de fractales
# que puede generar. Puede investigar y experimentar con otros tipos de fractales,
# como el conjunto de Julia, los fractales de L-system, y más.
# Este código es un ejemplo básico y puede necesitar ajustes según sus necesidades específicas.
# Además, para fractales más complejos, considere usar bibliotecas especializadas
# como PIL (Pillow) para manipulación de imágenes o OpenGL para renderizado avanzado.
# Asegúrese de tener Python instalado en su sistema para ejecutar este código.
# Puede ejecutar este script en la terminal o en un entorno de desarrollo integrado (IDE).