# Evite cláusulas except demasiado amplias
""" Aunque puede ser tentador capturar todas las excepciones utilizando una 
    cláusula except: (como capturar todos los tipos de peces en una red), 
    generalmente se desaconseja. 
    Este enfoque puede ocultar la verdadera naturaleza de los errores y convertir 
    la depuración en una pesadilla. """

try:
    result = some_function()  # This function might raise various exceptions
except:
    print("An error occurred")  # Hides the actual problem

""" En este ejemplo, si some_function() lanza un TypeError o un ValueError, 
    se imprimirá el mensaje de error genérico "Se ha producido un error", 
    ocultando la verdadera causa del problema. """