""" Día 38: Excepciones personalizadas
Crea una clase de excepción personalizada. """

class CustomError(Exception):
    """Clase de excepción personalizada que hereda de Exception."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
def risky_function(value):
    """Función que lanza una excepción personalizada si el valor es negativo."""
    if value < 0:
        raise CustomError("El valor no puede ser negativo.")
    return value * 2
try:
    result = risky_function(-5)
    print(f"Resultado: {result}")
except CustomError as e:
    print(f"Se ha producido un error personalizado: {e.message}")

# Salida esperada:
# Se ha producido un error personalizado: El valor no puede ser negativo.