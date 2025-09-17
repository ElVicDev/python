""" Día 61: Programación dinámica
Implementar programación dinámica para Fibonacci. """

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Ejemplo de uso
n = 10
print(f"El {n}º número de Fibonacci es: {fibonacci(n)}")

# Output:
# El 10º número de Fibonacci es: 55
# Comparación con el código del día 60:
# El código del día 60 resuelve el problema de la Torre de Hanoi utilizando recursión,
# mientras que este código del día 61 utiliza programación dinámica para calcular
# números de Fibonacci de manera eficiente.