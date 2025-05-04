while True:
    line = input('> ')   # Ingresaremos cualquier texto que deseamos
    if line == 'done' :   # Hasta que no escribamos done no sale del bucle
        break   # Rompe el bucle infinito y continua leyendo la siguiente línea
    print(line)
print('Done!')