while True:
    line = input('> ')   # Ingresaremos cualquier texto que deseamos
    if line[0] == '#' :   # Si escribimos # dejara de repetir lo que escribimos
        continue     # # Rompe el bucle infinito y continua con la siguiente línea
    if line == 'done' :   # Hasta que no escribamos done no sale del bucle
        break   # Rompe el bucle infinito y continua leyendo la siguiente línea
    print(line)
print('Done!')