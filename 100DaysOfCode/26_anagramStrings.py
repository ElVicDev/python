""" Día 26: cuerdas de anagrama
Escriba una función de verificación si dos cadenas son anagramas. """
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
str1_input = input("Ingrese la primera cadena: ")
str2_input = input("Ingrese la segunda cadena: ")
if are_anagrams(str1_input, str2_input):
    print(f'"{str1_input}" y "{str2_input}" son anagramas.')
else:
    print(f'"{str1_input}" y "{str2_input}" no son anagramas.')
# Ejemplo de uso
# Ingrese la primera cadena: escucha
# Ingrese la segunda cadena: escucha
# "escucha" y "escucha" son anagramas.
# Ejemplo de uso
# Ingrese la primera cadena: Dormitory
# Ingrese la segunda cadena: Dirty room
# "Dormitory" y "Dirty room" son anagramas.
# Ejemplo de uso
# Ingrese la primera cadena: hola
# Ingrese la segunda cadena: mundo
# "hola" y "mundo" no son anagramas.