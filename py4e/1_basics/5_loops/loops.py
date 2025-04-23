n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
print(n)
# ____________________________________________________________________
while True:
    line = input('> ')   # Ingresaremos cualquier texto que deseamos
    if line == 'done' :   # Hasta que no escribamos done no sale del bucle
        break   # Rompe el bucle infinito y continua leyendo la siguiente línea
    print(line)
print('Done!')
# ___________________________________________________________________
while True:
    line = input('> ')   # Ingresaremos cualquier texto que deseamos
    if line[0] == '#' :   # Si escribimos # dejara de repetir lo que escribimos
        continue     # # Rompe el bucle infinito y continua con la siguiente línea
    if line == 'done' :   # Hasta que no escribamos done no sale del bucle
        break   # Rompe el bucle infinito y continua leyendo la siguiente línea
    print(line)
print('Done!')
# ___________________________________________________________________
print('Se utilizó el bucle for para imprimir uns lista de números')
for i in [5, 4, 3, 2, 1] :  # Este es otro tipo de bucle utilizando for
    print(i)
print('Blastoff!')
# ___________________________________________________________________
print('El siguiente bucle le da Feliz Año a una lista de amigos')
friends =['Joseph', 'Glenn', 'Sally']   # Cadena con lista de amigos
for friend in friends :                 # iniciamos el bucle con for
    print('Happy New Year: ', friend)   # Imprime una linea por cada amigo
print('Done!')
# ___________________________________________________________________
# Blucle que busca el número mayor
print('El siguiente programa utiliza un bucle que busca el número mayor')
largest_so_far = -1     # empezamos dando un numero negativo cualquiera
print('Before', largest_so_far)
for the_num in [9, 41,12,3,74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)
# ___________________________________________________________________
# Blucle que busca el número menor
print('El siguiente programa utiliza un bucle que busca el número menor')
smallest = None     # empezamos asignando None para determinar que no hay numero
print('Before')
for the_num in [9, 41,12,3,74,15] :
    if smallest is None :     # is es similar a == pero mas fuerte
                              # tambien podemos ocupar en otro programa is note
                              # que es lo contrario a is
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
# ___________________________________________________________________
print('El siguiente programa enumero las iteraciones hechas con for')
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('after', zork)
# ___________________________________________________________________
print('El siguiente programa suma los números de una lista dada')
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('after', zork)
# ___________________________________________________________________
print('El siguiente programa encuentra el promedio entre count y sum')
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum / count)
# ___________________________________________________________________
print('Este bucle encuentra los numeros mas grandes a 20 de una lista dada')
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
        print('Large number', value)
print('After')
# ___________________________________________________________________
print('Este bucle cambia la variable de FALSE a TRUE cuando encuentra un numero')
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
        print(found, value)
print('After', found)
