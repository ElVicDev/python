""" Escribir un programa Python que calcule el precio final de un artículo después de aplicar un descuento.
    El precio original del artículo es de 75$.
    El descuento es del 15%.

Su programa debe:
    - Almacenar el precio original y el descuento en variables.
    - Calcular el descuento dividiendo discount_rate entre 100 y multiplicando por original_price.
    - Calcular el precio final restando discount de original_price. 
    - Imprima el precio final con un mensaje claro.

Resultado esperado:
El precio final después del descuento es: $63.75 """

original_price = 75
discount_rate = 15

discount = (discount_rate / 100) * original_price
final_price = original_price - discount

print("The final price after discount is: $", final_price)