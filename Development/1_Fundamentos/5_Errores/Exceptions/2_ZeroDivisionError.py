# ZeroDivisionError
""" Esta excepción se produce cuando se intenta dividir un número por cero. """

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except TypeError:
    print("Error: Invalid data types")

""" En este ejemplo, tenemos dos bloques except, cada uno diseñado para atrapar 
    un tipo específico de excepción. 
    Si intentamos dividir por cero, se ejecutará el bloque ZeroDivisionError. 
    Si intentamos realizar una operación con tipos incompatibles, se ejecutará 
    el bloque TypeError. """