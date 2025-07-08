'''
  Escriba un programa para leer el mbox-short.txt y
  averiguar quién ha enviado la mayor cantidad de mensajes de correo.
  El programa busca líneas 'De' y toma la segunda palabra
  de esas líneas como la persona que envió el correo.
  El programa crea un diccionario de Python que asigna la dirección
  de correo del remitente a un recuento de la cantidad de veces que aparecen en el archivo.
  Después de generar el diccionario, el programa lee el diccionario utilizando
  un ciclo máximo para encontrar el autor de confirmación más prolífico.
'''

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds:
        di[w] = di.get(w,0) + 1

largest = -1
theword = None
for k,v in di.items() :
    # print(k,v)
    if v > largest :
        largest = v
        theword = k # Capture/remember the key that was largest

print(theword,largest)
