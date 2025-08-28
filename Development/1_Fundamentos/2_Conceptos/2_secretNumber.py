""" Adivina el número secreto
    Crear un juego de adivinar números en el que el ordenador intentará adivinar 
    un número secreto que usted le indique. 
    El ordenador generará conjeturas aleatorias dentro de un rango (1 a 10) 
    y continuará adivinando hasta que encuentre el número correcto.
Instrucciones:
    - Configure su secret_number:
        Elija un número entre 1 y 10 y asígnele una variable llamada secret_number. 
        No lo asigne al azar; elija un número para poder verificar que el código 
        funciona.
    - Inicializa otra variable llamada guess con un valor de 0.
    - Completa el bucle while: 
        Añada la condición al bucle while para asegurarse de que continúa 
        ejecutándose mientras guess no sea igual a su secret_number. """

import random

# Set the secret_number variable here (between 1 and 10)
secret_number = 7
# Initialize the guess variable here with a value of 0
guess = 0
while guess != secret_number:  # Add the while loop condition here
	guess = random.randint(1, 10)
	print("Guessing:",guess)

print("I guessed the right number! It was",secret_number)