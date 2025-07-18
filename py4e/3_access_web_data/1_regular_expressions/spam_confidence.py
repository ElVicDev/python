# Buaca en el archivo mbox-short.txt las lineas que empiecen con X-DSPAM-Confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
                                    # ([0-9.]+) incluye todo lo que este en este rango del 0 al 9
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))    # nos imprime el número mas alto encontrado de la lista
