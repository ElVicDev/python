""" NÚMERO IMPAR
Escribe un programa en Python que tome una lista de números e itere por cada 
número y compruebe si es par o impar. 
Utiliza la lista de números proporcionada como punto de partida.
    - Iterar sobre la lista de números: Utilice un bucle for para iterar sobre 
        la lista proporcionada (for number in numbers:). 
        Utilice el nombre de variable number para la variable.
    - Comprobar par/impar: Utilice una sentencia condicional para determinar 
        si cada número es par o impar.
    - Mostrar salida: 
        Imprima un mensaje indicando si los números son pares o impares.

Consejos:
    - Puede utilizar el operador de módulo (%) para comprobar si un 
        número es divisible por 2.
    - Si el resto de la división por 2 es 0, el número es par.
    - En caso contrario, es impar.

Ejemplo de entrada:
    números = [3, 9, 1, 10, 5, 2, 8]

Resultado esperado:
    3 es impar
    9 es impar
    1 es impar
    10 es par
    5 es impar
    2 es par
    8 es par
"""

numbers = [3, 9, 1, 10, 5, 2, 8]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} es par")
    else:
        print(f"{number} es impar")