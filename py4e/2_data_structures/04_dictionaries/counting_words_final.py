'''
  Escriba un programa para leer el mbox-short.txt y
  averiguar quién ha enviado la mayor cantidad de mensajes de correo.
  El programa busca líneas 'From' y toma la segunda palabra
  de esas líneas como la persona que envió el correo.
  El programa crea un diccionario de Python que asigna la dirección
  de correo del remitente a un recuento de la cantidad de veces que aparecen en el archivo.
  Después de generar el diccionario, el programa lee el diccionario utilizando
  un ciclo máximo para encontrar el autor de confirmación más prolífico.
'''

filename = input("Enter file:")
if len(filename) < 1 : filename = "mbox-short.txt"
handle = open(filename)
counts = dict()
for line in handle:
    line = line.strip()
    if line.startswith('From ') :
        sender = line.split()
        email = sender[1]
        counts[email] = counts.get(email,0) + 1
    else:
        continue

bigcount = None
bigsender = None
for email,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigsender = email
        bigcount = count

print (bigsender, bigcount)
