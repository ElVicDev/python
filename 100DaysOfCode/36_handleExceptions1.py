""" Día 36: Manejar excepciones 1
Manejar excepciones para la división por cero. """

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    else:
        return f'El resultado de {num1} dividido por {num2} es {result}.'

# Pruebas
print(divide_numbers(10, 2))  # Salida esperada: El resultado de 10 dividido por 2 es 5.0.
print(divide_numbers(10, 0))  # Salida esperada: Error: No se puede dividir por cero.
print(divide_numbers(15, 3))  # Salida esperada: El resultado de 15 dividido por 3 es 5.0.
print(divide_numbers(7, -1))  # Salida esperada: El resultado de 7 dividido por -1 es -7.0.
print(divide_numbers(0, 5))   # Salida esperada: El resultado de 0 dividido por 5 es 0.0.