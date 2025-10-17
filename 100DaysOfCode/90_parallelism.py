""" Día 90: Concurrencia y paralelismo
Explore la concurrencia y el paralelismo con Python 
(por ejemplo, subprocesamiento, multiprocesamiento). """

import concurrent.futures
import time
import math
def is_prime(n):
    """Función para verificar si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def find_primes_in_range(start, end):
    """Función para encontrar todos los números primos en un rango dado."""
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes
if __name__ == "__main__":
    start_time = time.time()
    range_start = 10**6
    range_end = 10**6 + 10000
    num_workers = 4
    chunk_size = (range_end - range_start) // num_workers
    ranges = [(range_start + i * chunk_size, range_start + (i + 1) * chunk_size) for i in range(num_workers)]
    all_primes = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(find_primes_in_range, r[0], r[1]) for r in ranges]
        for future in concurrent.futures.as_completed(futures):
            all_primes.extend(future.result())
    end_time = time.time()
    print(f"Números primos encontrados: {all_primes}")
    print(f"Tiempo total: {end_time - start_time} segundos")
""" Resultados esperados:
El programa imprimirá una lista de números primos encontrados en el rango especificado y el tiempo total tomado para completar la tarea.
"""
# Nota: Asegúrese de tener Python instalado en su sistema para ejecutar este código.
# Puede ejecutar este script en la terminal o en un entorno de desarrollo integrado (IDE).
# Este código utiliza el módulo concurrent.futures para paralelizar la búsqueda de números primos
# en un rango grande. Ajuste los parámetros range_start, range_end y num_workers según
# sus necesidades y capacidades de hardware.
# Tenga en cuenta que el uso de multiprocesamiento puede no ser eficiente para tareas
# muy pequeñas debido a la sobrecarga de crear procesos adicionales.
# Este ejemplo es básico y puede necesitar ajustes según sus necesidades específicas.
# Además, para tareas más complejas, considere usar bibliotecas especializadas
# como Dask o Ray para manejar la concurrencia y el paralelismo de manera más eficiente.
# Asegúrese de ejecutar este código en un entorno adecuado que soporte multiprocesamiento
# como una terminal o un IDE, ya que algunos entornos como Jupyter Notebook
# pueden tener limitaciones con el multiprocesamiento.
# El código anterior encuentra números primos en un rango grande utilizando
# múltiples procesos para acelerar la tarea. Puede experimentar con diferentes
# rangos y números de trabajadores para ver cómo afecta el rendimiento.
# Además, tenga en cuenta que el rendimiento puede variar según la carga de trabajo
# y las capacidades de hardware de su sistema.