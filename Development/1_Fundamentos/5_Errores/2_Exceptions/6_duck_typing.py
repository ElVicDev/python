# Tipado de patos: La flexibilidad y sus retos
""" Python adopta el concepto de "tipado de pato", que se centra en cómo se 
    comporta un objeto más que en su tipo estricto. 
    Esta flexibilidad es un arma de doble filo. 
    Permite un código dinámico y adaptable, pero también puede dar lugar a 
    errores inesperados en tiempo de ejecución cuando los objetos no se 
    comportan como se esperaba. """

def calculate_area(shape):
    try:
        return shape.calculate_area()
    except AttributeError:
        raise TypeError("Object does not have a calculate_area method")
    
""" En este ejemplo, intentamos llamar a calculate_area con un objeto pasado 
    como shape. 
    Si el objeto no tiene este método (tal vez no es una forma geométrica), 
    se producirá un error AttributeError. 
    Lo detectamos y lanzamos un mensaje más informativo TypeError, 
    indicando que el objeto no es adecuado para el cálculo. """