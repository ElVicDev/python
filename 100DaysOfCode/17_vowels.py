""" Día 17: Número de vocales en una cuerda
Escriba una función para contar el número de vocales en una cadena. """
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

string = input("Ingrese una cadena para contar las vocales: ")
print(f"La cadena '{string}' tiene {count_vowels(string)} vocales.")

# Ejemplo de uso
# Ingrese una cadena para contar las vocales: Hola Mundo
# La cadena 'Hola Mundo' tiene 4 vocales.

# Ejemplo de uso
# Ingrese una cadena para contar las vocales: Python es divertido
# La cadena 'Python es divertido' tiene 6 vocales.

# Ejemplo de uso
# Ingrese una cadena para contar las vocales: 12345
# La cadena '12345' tiene 0 vocales.