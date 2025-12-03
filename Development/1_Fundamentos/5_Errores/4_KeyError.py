# KeyError
""" Ocurre cuando intentas acceder a un valor en un diccionario usando 
    una clave que no existe. """

""" Puede utilizar un bloque try-except para capturar un KeyError y proporcionar 
    un comportamiento alternativo cuando no se encuentra una clave. """

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError:
    print("Key not found in dictionary.")

""" Un KeyError no controlado en un entorno de producción puede provocar 
    un comportamiento inesperado del programa o incluso su bloqueo. """