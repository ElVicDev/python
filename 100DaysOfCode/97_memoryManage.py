""" Día 97: Gestión de memoria y recolección de basura.
Obtenga información sobre la gestión de memoria 
y la recolección de basura de Python. """

import sys
import gc
# Función para mostrar el uso de memoria de un objeto
def show_memory_usage(obj, obj_name):
    size = sys.getsizeof(obj)
    print(f"Uso de memoria de {obj_name}: {size} bytes")
# Crear una lista grande para demostrar el uso de memoria
large_list = [i for i in range(100000)]
show_memory_usage(large_list, "large_list")
# Forzar la recolección de basura
gc.collect()
print("Recolección de basura forzada.")
""" Resultados esperados:
El programa imprimirá el uso de memoria de la lista grande creada y confirmará
que se ha forzado la recolección de basura. """
# Nota: Este código demuestra cómo verificar el uso de memoria de los objetos
# en Python y cómo forzar la recolección de basura utilizando el módulo gc.
# Puede ejecutar este código en cualquier entorno Python sin necesidad
# de bibliotecas adicionales.