""" Día 13: El más grande de tres números.
Escriba un programa para encontrar el más grande de tres números. """

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} es el número más grande.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} es el número más grande.")
else:
    print(f"{num3} es el número más grande.")
