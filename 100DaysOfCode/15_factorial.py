""" Día 15: Factorial
Escriba una función para calcular el factorial de un número. """
def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

number = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {number} es {factorial(number)}.")

# Ejemplo de uso
# Ingrese un número para calcular su factorial: 5
# El factorial de 5 es 120.

# Ejemplo de uso
# Ingrese un número para calcular su factorial: 0
# El factorial de 0 es 1.

# Ejemplo de uso
# Ingrese un número para calcular su factorial: -3
# El factorial no está definido para números negativos.