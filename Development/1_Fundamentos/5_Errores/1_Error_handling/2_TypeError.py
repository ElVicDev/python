# TypeError
""" Suele aparecer cuando se intenta combinar o manipular datos de formas 
    que Python no permite. """

def calculate_area(length, width): 
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)): 
        raise TypeError("Length and width must be numbers.") 
    return length * width

print(calculate_area(5, 'three')) # TypeError: Length and width must be numbers.

""" Si un TypeError no se comprueba en la producción, podría desencadenar una 
    cascada de errores, provocando un comportamiento inesperado del programa 
    y corrompiendo potencialmente las estructuras de datos. 
    Por ejemplo, si una función espera una lista pero recibe una cadena, 
    podría intentar iterar sobre los caracteres de la cadena, lo que provocaría 
    resultados inesperados o incluso el bloqueo del programa. """