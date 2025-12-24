# Técnicas de depuración

""" def calculatediscount(price, percentage):
        if percentage < 0 or percentage > 100:
            return "Invalid discount percentage" # Incorrect behavior
        discountamount = price * (percentage / 100)
        return price - discountamount
    print(calculatediscount(100, 150)) # Should be an error 
"""
# El problema es que la función devuelve incorrectamente una cadena cuando 
# el porcentaje de descuento no es válido. 
# En su lugar, debería lanzar una excepción para señalar una condición de error.

def calculate_discount(price, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_amount = price * (percentage / 100)
    return price - discount_amount
try:
    print(calculate_discount(100, 150))
except ValueError as e:
    print(f"Error: {e}") # Error: Discount percentage must be between 0 and 100