""" Día 35: Operaciones de archivo
Calcule el promedio de números en un archivo de texto. """

# Crear y escribir en un archivo de texto
with open('numbers.txt', 'w') as file:
    file.write('10\n20\n30\n40\n50\n')
    file.write('60\n70\n80\n90\n100\n')
    file.write('110\n120\n130\n140\n150\n')
    file.write('160\n170\n180\n190\n200\n')
    file.write('210\n220\n230\n240\n250\n')
    file.write('260\n270\n280\n290\n300\n')
    file.write('310\n320\n330\n340\n350\n')
    file.write('360\n370\n380\n390\n400\n')
    file.write('410\n420\n430\n440\n450\n')
    file.write('460\n470\n480\n490\n500\n')

# Leer el archivo y calcular el promedio
with open('numbers.txt', 'r') as file:
    numbers = file.readlines()
    numbers = [int(num.strip()) for num in numbers]
    average = sum(numbers) / len(numbers)
    print(f'El promedio de los números en el archivo es: {average}')

# Salida esperada: El promedio de los números en el archivo es: 255.0
# (dependiendo de los números escritos en el archivo)