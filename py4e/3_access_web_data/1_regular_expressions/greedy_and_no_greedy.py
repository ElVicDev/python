# se debe agregar primero la biblioteca de expresiones regulares
import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)    # Usamos expresiónes regulares para la búsqueda ^F.+:
print(y)        # Nos devuelve el resultado mas largo, From: Using the :

y = re.findall('^F.+?:', x)   # Agregamos un ? después del + para indicarle que no sea codicioso
print(y)        # Nos devuelve el resultado mas corto, From:
