""" Crear un diccionario Python para representar un simple catálogo de productos. 
    El diccionario debe contener tres productos, con el SKU 
    (Unidad de mantenimiento de existencias) de cada producto como clave. """

# Add the SKU data provided to the product catalog dictionary
product_catalog = {
    "SKU123": {"name": "Widget A", "price": 19.99, "amount": 50},
    "SKU456": {"name": "Gadget B", "price": 34.95, "amount": 25},
    "SKU789": {"name": "Gizmo C", "price": 9.99, "amount": 100}
} 

# Look up this SKU in your code. 
sku_to_find = "SKU123"

if sku_to_find in product_catalog:
    # Acceder a los detalles del producto usando la SKU como clave
    product_details = product_catalog[sku_to_find]

    # Extraer el nombre y el precio
    name = product_details["name"]
    price = product_details["price"]

    # Imprimir el resultado usando una f-string para un formato claro
    # Nota: El formato '.2f' asegura que el precio se muestre con dos decimales.
    print(f"The price of {name} is ${price:.2f}")

else:
    # Manejo de errores en caso de que la SKU no se encuentre en el catálogo
    print(f"Error: No se encontró un producto con la SKU '{sku_to_find}' en el catálogo.")