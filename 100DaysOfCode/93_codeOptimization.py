""" Día 93: Optimización del código
Optimice el código para el rendimiento 
(por ejemplo, creación de perfiles, técnicas de optimización). """

import time
import cProfile

def slow_function():
    """Función que simula un proceso lento."""
    total = 0
    for i in range(1, 10000):
        for j in range(1, 1000):
            total += i * j
    return total

def optimized_function():
    """Función optimizada utilizando técnicas de reducción de complejidad."""
    total = 0
    for i in range(1, 10000):
        total += i * sum(range(1, 1000))
    return total

if __name__ == "__main__":
    # Medir el tiempo de la función lenta
    start_time = time.time()
    slow_result = slow_function()
    slow_duration = time.time() - start_time
    print(f"Slow function result: {slow_result} in {slow_duration:.4f} seconds")

    # Medir el tiempo de la función optimizada
    start_time = time.time()
    optimized_result = optimized_function()
    optimized_duration = time.time() - start_time
    print(f"Optimized function result: {optimized_result} in {optimized_duration:.4f} seconds")

    # Perfilado de la función lenta
    print("\nProfiling slow_function:")
    cProfile.run('slow_function()')

    # Perfilado de la función optimizada
    print("\nProfiling optimized_function:")
    cProfile.run('optimized_function()')

""" Resultados esperados:
El programa imprimirá los resultados de ambas funciones junto con el tiempo que
tardaron en ejecutarse. La función optimizada debería ser significativamente más
rápida que la función lenta. Además, se mostrarán los perfiles de ambas funciones,
lo que permitirá comparar su rendimiento en detalle. """
# Nota: Este código demuestra cómo optimizar una función para mejorar su rendimiento.
# Utiliza técnicas de reducción de complejidad y perfilado para identificar 
# cuellos de botella en el código. 
# Puede ejecutar este código en cualquier entorno Python sin necesidad de 
# bibliotecas adicionales.