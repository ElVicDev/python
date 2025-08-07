""" Día 16: Cadena de Palindrome
Escriba una función para verificar si una cadena dada es un palíndromo. """
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

string = input("Ingrese una cadena para verificar si es un palíndromo: ")
print(f"La cadena '{string}' es un palíndromo: {is_palindrome(string)}.")

# Ejemplo de uso
# Ingrese una cadena para verificar si es un palíndromo: Anilina
# La cadena 'Anilina' es un palíndromo: True.

# Ejemplo de uso
# Ingrese una cadena para verificar si es un palíndromo: Hola
# La cadena 'Hola' es un palíndromo: False.
