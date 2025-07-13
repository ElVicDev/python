""" se debe agregar primero la biblioteca de expresiones regulares """
import re

x = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)    
# \S sin espacios
# @ la frase debe de contener una arroba
# + indica que sea codicioso hacia la derecha y hacia la izquierda """
print(y)

a = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
b = re.findall('^From: (\S+@\S+)', a)    
# la busqueda exacta nos regresaría
# From: stephen.marquard@uct.ac.za
# los parentesis indican el inicio y el fin de la extracción
# por lo que el resultado que nos dará es el email solamente
print(b)
