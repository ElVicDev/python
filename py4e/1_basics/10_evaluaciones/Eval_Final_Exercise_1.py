print("Programa que pide al usuario números hasta que se ingrese 'done'.")
print("Al final, imprime la suma y el promedio de los números ingresados.")
print("Maneja excepciones para entradas no válidas.")

num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except ValueError:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval
print(tot, " / ", num, " = ", tot/num)
