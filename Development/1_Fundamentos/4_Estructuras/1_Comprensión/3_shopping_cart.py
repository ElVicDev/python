""" Escribir un programa en Python que almacene una lista de artículos 
en un carrito de la compra utilizando una estructura de datos mutable y, 
a continuación, imprima el contenido del carrito. """

# Carrito de la compra como una lista
shopping_cart = []
# Función para agregar artículos al carrito
def add_to_cart(item):
    shopping_cart.append(item)
# Función para imprimir el contenido del carrito
def print_cart():
    print("Contenido del carrito de la compra:")
    for item in shopping_cart:
        print("- " + item)
# Agregar algunos artículos al carrito
add_to_cart("manzanas")
add_to_cart("plátanos")
add_to_cart("leche")
# Imprimir el contenido del carrito
print_cart()
""" Resultado esperado:
El programa imprimirá el contenido del carrito de la compra:
Contenido del carrito de la compra:
- manzanas
- plátanos
- leche
"""