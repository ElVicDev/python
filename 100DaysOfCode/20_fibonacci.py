""" Día 20: Secuencia de Fibonacci
Escriba una función para calcular la secuencia de Fibonacci hasta cierto límite. """
def fibonacci_sequence(limit):
    if limit < 0:
        return []
    elif limit == 0:
        return [0]
    elif limit == 1:
        return [0, 1]
    fib_seq = [0, 1]
    while True:
        next_value = fib_seq[-1] + fib_seq[-2]
        if next_value > limit:
            break
        fib_seq.append(next_value)
    return fib_seq

limit = int(input("Ingrese un límite para la secuencia de Fibonacci: "))
fib_seq = fibonacci_sequence(limit)
print(f"La secuencia de Fibonacci hasta {limit} es: {fib_seq}.")
# Ejemplo de uso
# Ingrese un límite para la secuencia de Fibonacci: 10
# La secuencia de Fibonacci hasta 10 es: [0, 1, 1, 2, 3, 5, 8].

# Ejemplo de uso
# Ingrese un límite para la secuencia de Fibonacci: 20
# La secuencia de Fibonacci hasta 20 es: [0, 1, 1, 2, 3, 5, 8, 13].

# Ejemplo de uso
# Ingrese un límite para la secuencia de Fibonacci: 50
# La secuencia de Fibonacci hasta 50 es: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].