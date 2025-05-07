# Escriba un programa que solicite repetidamente al usuario
# números enteros hasta que el usuario ingrese 'done'.
# Una vez que haya ingresado 'done',
# imprima el mayor y el menor de los números.
# Si el usuario ingresa algo que no sea un número válido,
# atrápelo con un intento/excepto y
# emita un mensaje apropiado e ignore el número.
# Ingrese 7, 2, bob, 10 y 4 y haga coincidir el resultado a continuación.

largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
        if largest is None or largest < num:
            largest = num
        if smallest is None or smallest > num:
            smallest = num
    except ValueError:
        print('Invalid input')
        continue

print('Maximum is', largest)
print('Minimum is', smallest)