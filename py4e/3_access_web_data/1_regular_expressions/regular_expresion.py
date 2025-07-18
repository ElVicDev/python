# se debe agregar primero la biblioteca de expresiones regulares
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*: ', line) :   # Usamos expresiónes regulares para la búsqueda ^X.*:
        print(line)
