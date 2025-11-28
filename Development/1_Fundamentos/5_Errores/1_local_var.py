""" Problemas de alcance:
    Las variables tienen una vida útil y una visibilidad limitadas, 
    lo que se conoce como su ámbito. 
    Intentar acceder a una variable fuera de su ámbito es como intentar 
    encontrar un libro en una biblioteca que no lo tiene.  """

def myfunction():
    local_var = 10
print(local_var) # NameError: name 'local_var' is not defined

""" Aquí, local_var sólo existe dentro del ámbito de my_function. 
    Intentar acceder a ella fuera de la función da como resultado 
    un NameError porque no es visible en el ámbito global. """