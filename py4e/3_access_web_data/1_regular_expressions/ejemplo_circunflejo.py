# se debe agregar primero la biblioteca de expresiones regulares
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line) :   # Usamos el circunflejo como expresión regular para la búsqueda
        print(line)
