# Blucle que busca el número menor
print('El siguiente programa utiliza un bucle que busca el número menor')
smallest = None     # empezamos asignando None para determinar que no hay numero
print('Before')
for the_num in [9, 41,12,3,74,15] :
    if smallest is None :   # is es similar a == pero mas fuerte
                            # tambien podemos ocupar en otro programa is note
                            # que es lo contrario a is
        smallest = the_num
    elif the_num < smallest :
        smallest = the_num
    print(smallest, the_num)
print('After', smallest)