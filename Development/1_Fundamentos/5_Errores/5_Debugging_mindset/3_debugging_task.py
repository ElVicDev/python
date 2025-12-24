# Depuración de un cálculo defectuoso

""" Te han dado una función Python calculate_discount(price, discount_percentage) 
    que calcula el precio con descuento de un artículo. 
    Sin embargo, ¡algunos clientes están reportando resultados extraños!

Su tarea:
    Revisar la función calculate_discount.
    Añade la entrada de ejemplo a tu código e intenta ejecutarla.
    Observe el resultado e identifique el error.
    Corrija el error para que la función calcule el descuento correctamente.

Consejos:
    El precio final con descuento debe ser inferior al precio original.

Salida esperada (después de corregir el error):
40.0 """

def calculate_discount(price, discount_percentage):
    discount_amount = price * (discount_percentage / 100)
    discounted_price = price - discount_amount
    return discounted_price


# Code to test your output
price = 50
discount_percentage = 20
discounted_price = calculate_discount(price, discount_percentage)
print(discounted_price)