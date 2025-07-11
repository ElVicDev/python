'''
 Escribe un programa para leer el mbox-short.txt y calcular la distribución
 por hora del día para cada uno de los mensajes.
 Puede sacar la hora de la línea 'From' encontrando la hora y luego
 dividiendo la cadena por segunda vez usando dos puntos.
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
 Una vez que haya acumulado los conteos para cada hora,
 imprima los conteos, ordenados por hora como se muestra a continuación.
'''

name = input('Enter file: ')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)
di = dict()
li = list()
count = 0
for line in handle :
    if line.startswith('From') :
        if line.startswith('From: ') :
            continue
        else :
            count = count + 1
            lines = line.split()
            str = ''.join(lines[5])
            li.append(str[0:2])
for hour in li :
    di[hour] = di.get(hour,0) + 1
for v,k in sorted(di.items()) :
    print(v,k)
