""" Día 11: mientras
Use un bucle de tiempo para imprimir números pares de 2 a 20.
"""
number = 0
while number < 20:
    number += 1
    if number % 2 == 0:
        print(number)
else:
    print("Fin del bucle while.")
