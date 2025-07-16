# Ejemplo de extraer el domino usando find
data = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')          # El punto inicial es a partir de la arroba
sppos = data.find(' ', atpos)   # El punto final es el espacio
host = data[atpos+1 : sppos]    # Iprimira un lugar despues de la @ hasta donde encuentra un espacio
print(host)

# Otro ejemplo de extraer el dominio es usando split
data = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = data.split()            # Lo dividimos por espacios
email = words[1]                # Identificamos el email
pieces = email.split('@')       # Lo volvemos a dividir buscando la arroba
print(pieces[1])                # Imprimimos solo la parte del dominio

# Usando expresiones regulares también podemos extraer el dominio
import re
data = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', data) # [^ ] indica que todo lo que NO es espacio y despues de la arroba
print(y)                         # nos imprime el dominio ['uct.ac.za']

# podemos afinar la búsqueda del dominio empezando desde el From de la siguiente manera:
z = re.findall('^From: .*@([^ ]*)', data)
print(z)

# Otro ejemplo usando expresiones regulares para extraer el dominio
import re
data = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@(\\S+)', data) # extraé todo lo que NO es espacio y despues de la arroba
print(y)
